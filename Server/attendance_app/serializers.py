from rest_framework import serializers
from .models import Student, Class, AttendanceRecord


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name']


class AttendanceRecordSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = AttendanceRecord
        fields = ['student', 'attending']


class ClassSerializer(serializers.ModelSerializer):
    studentsList = AttendanceRecordSerializer(source='attendancerecord_set', many=True, read_only=True)

    class Meta:
        model = Class
        fields = ['period', 'schoolGrade', 'classMeta', 'teacher', 'studentsList']

    def create(self, validated_data):
        students_data = validated_data.pop('studentsList', [])
        class_instance = Class.objects.create(**validated_data)

        for student_data in students_data:
            student = Student.objects.get(id=student_data['student']['id'])
            AttendanceRecord.objects.create(
                classMeta=class_instance,
                student=student,
                attending=student_data['attending']
            )

        return class_instance

