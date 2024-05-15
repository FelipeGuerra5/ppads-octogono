from rest_framework import serializers
from .models import Class, Subject, Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'parent']

class StudentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name']

class SubjectSerializer(serializers.ModelSerializer):
    students = StudentNameSerializer(many=True)

    class Meta:
        model = Subject
        fields = ['id', 'name', 'classMeta', 'students']

class ClassSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Class
        fields = ['id', 'period', 'schoolGrade', 'classMeta', 'teacher', 'students', 'subjects']

class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name')
