from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Class, Subject, Student
from .serializers import SubjectSerializer, StudentSerializer, StudentListSerializer, \
    TeacherClassSerializer
from attendance_app.models import Statistics
from attendance_app.serializers import StatisticsSerializer


class ClassListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        teacher = request.user
        serializer = TeacherClassSerializer(teacher)
        return Response(serializer.data)


class ClassActionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, class_id):
        # Verificar se a classe existe
        class_instance = get_object_or_404(Class, id=class_id)

        # Obter a ação do corpo da requisição
        action = request.data.get('action')

        if action == "Fazer Chamada":
            return self.fazer_chamada(request, class_instance)
        elif action == "Verificar Estatísticas":
            return self.verificar_estatisticas(request, class_instance)
        elif action == "Ver Lista de Alunos":
            return self.ver_lista_alunos(request, class_instance)
        else:
            return Response({"message": "Ação inválida"}, status=status.HTTP_400_BAD_REQUEST)

    def fazer_chamada(self, request, class_instance):
        # Retornar a lista de alunos para marcar presença
        students = Student.objects.filter(classes=class_instance)
        serializer = StudentListSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def verificar_estatisticas(self, request, class_instance):
        # Retornar as estatísticas de presença da classe
        statistics = Statistics.objects.filter(classMeta=class_instance)
        serializer = StatisticsSerializer(statistics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def ver_lista_alunos(self, request, class_instance):
        # Retornar a lista de alunos na classe
        students = Student.objects.filter(classes=class_instance)
        serializer = StudentListSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

