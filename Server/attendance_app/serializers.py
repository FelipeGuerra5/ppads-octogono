from rest_framework import serializers
from django.db import transaction
from classes.models import Class, Student
from attendance_app.models import AttendanceRecord, Statistics
from users.models import Teacher  # Corrigida a importação

class StudentAttendanceSerializer(serializers.Serializer):
    student = serializers.IntegerField()
    attending = serializers.BooleanField()


class ClassAttendanceSerializer(serializers.Serializer):
    date = serializers.DateField()
    studentsList = StudentAttendanceSerializer(many=True)

    def create(self, validated_data):
        students_data = validated_data.pop('studentsList')
        class_instance = self.context['class_instance']

        with transaction.atomic():
            for student_data in students_data:
                student = Student.objects.get(pk=student_data['student'])
                AttendanceRecord.objects.update_or_create(
                    classMeta=class_instance,
                    student=student,
                    date=validated_data['date'],
                    defaults={'attending': student_data['attending']}
                )
        return class_instance

class AttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = ['id', 'classMeta', 'student', 'attending', 'date']

class StatisticsSerializer(serializers.ModelSerializer):
    attendance_percentage = serializers.ReadOnlyField()

    class Meta:
        model = Statistics
        fields = ['id', 'student', 'classMeta', 'total_classes', 'attended_classes', 'attendance_percentage']

class StudentListSerializer(serializers.ModelSerializer):
    attending = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ('id', 'name', 'attending')

    def get_attending(self, obj):
        date = self.context.get('date')
        attendance_record = AttendanceRecord.objects.filter(student=obj, date=date).first()
        return attendance_record.attending if attendance_record else None
