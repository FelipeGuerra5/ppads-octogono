from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Teacher, Student, Class, AttendanceRecord


class AttendanceTests(APITestCase):
    def setUp(self):
        # Configuração comum para todos os testes nesta classe
        self.teacher = Teacher.objects.create(name="Fernanda")
        self.cls = Class.objects.create(period="afternoon", schoolGrade=6, classMeta="Português", teacher=self.teacher)
        self.student1 = Student.objects.create(name="João")
        self.student2 = Student.objects.create(name="Maria")
        AttendanceRecord.objects.create(classMeta=self.cls, student=self.student1, attending=True)
        AttendanceRecord.objects.create(classMeta=self.cls, student=self.student2, attending=False)

        self.record_attendance_url = reverse('record-attendance')
        self.record_attendance_data = {
            "period": "afternoon",
            "schoolGrade": 6,
            "classMeta": "Português",
            "teacher": self.teacher.id,
            "studentsList": [
                {"student": self.student1.id, "attending": True},
                {"student": self.student2.id, "attending": True},
            ]
        }

    def test_list_students(self):
        """
        Testa se a API de listar alunos retorna a resposta esperada para dados válidos.
        """
        list_students_url = reverse('list-students') + '?period=afternoon&schoolGrade=6'
        response = self.client.get(list_students_url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_record_attendance(self):
        """
        Testa se a API de registrar presença funciona como esperado.
        """
        response = self.client.post(self.record_attendance_url, self.record_attendance_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['recorded'])
