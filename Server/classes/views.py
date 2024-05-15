from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Class, Subject, Student
from .serializers import ClassSerializer, SubjectSerializer, StudentSerializer

class ClassListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        classes = Class.objects.filter(teacher=request.user)
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)

class ClassActionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, class_id):
        class_instance = get_object_or_404(Class, id=class_id)
        actions = ["Fazer Chamada", "Verificar Estatísticas", "Ver Lista de Alunos"]
        return Response({"actions": actions})

class StudentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, class_id):
        class_instance = get_object_or_404(Class, id=class_id)
        students = Student.objects.filter(classes=class_instance)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

class StudentSubjectListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        subjects = Subject.objects.filter(students=student)
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

