from rest_framework import serializers
from django.db import transaction
from .models import Class, AttendanceRecord, Student, Teacher


class StudentAttendanceSerializer(serializers.Serializer):
    student = serializers.IntegerField()
    attending = serializers.BooleanField()


class ClassAttendanceSerializer(serializers.Serializer):
    period = serializers.CharField(max_length=50)
    schoolGrade = serializers.IntegerField()
    classMeta = serializers.CharField(max_length=100)
    teacher = serializers.IntegerField()
    date = serializers.DateField()
    studentsList = StudentAttendanceSerializer(many=True)

    def create(self, validated_data):
        students_data = validated_data.pop('studentsList')
        teacher_id = validated_data.pop('teacher')

        # Usando o ID do professor para obter a instância do Professor
        teacher = Teacher.objects.get(pk=teacher_id)

        with transaction.atomic():
            class_instance, _ = Class.objects.get_or_create(
                period=validated_data['period'],
                schoolGrade=validated_data['schoolGrade'],
                classMeta=validated_data['classMeta'],
                teacher=teacher
            )

            for student_data in students_data:
                student = Student.objects.get(pk=student_data['student'])
                AttendanceRecord.objects.update_or_create(
                    classMeta=class_instance,
                    student=student,
                    date=validated_data['date'],
                    defaults={'attending': student_data['attending']}
                )
        return class_instance

class StudentListSerializer(serializers.ModelSerializer):
    attending = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ('id', 'name', 'attending')

    def get_attending(self, obj):
        # Assumindo que 'context' tem a data especificada para filtrar
        date = self.context.get('date')
        attendance_record = AttendanceRecord.objects.filter(student=obj, date=date).first()
        return attendance_record.attending if attendance_record else None
