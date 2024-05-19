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

class ClassDetailSerializer(serializers.ModelSerializer):
    Room = serializers.SerializerMethodField()

    class Meta:
        model = Class
        fields = ['id', 'classMeta', 'Room', 'schoolGrade', 'period']

    def get_Room(self, obj):
        # Aqui você pode personalizar como o nome da sala é obtido.
        return f"L{obj.schoolGrade}"

class TeacherClassSerializer(serializers.Serializer):
    teacher = serializers.CharField(source='name')
    teacherId = serializers.IntegerField(source='id')
    classes = ClassDetailSerializer(many=True, source='class_set')

class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name')
