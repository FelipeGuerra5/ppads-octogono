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

        # Ajustar conforme os novos endpoints e dados esperados
        self.record_attendance_url = reverse('register-attendance')
        self.view_attendance_url = reverse('view-attendance')

        self.record_attendance_data = {
            "period": "afternoon",
            "schoolGrade": 6,
            "classMeta": "Português",
            "teacher": self.teacher.id,
            "date": "2023-10-12",
            "attendance": True,
            "studentsList": [
                {"student": self.student1.id, "attending": True},
                {"student": self.student2.id, "attending": True},
            ]
        }

    def test_record_attendance(self):
        """
        Testa se a API de registrar presença funciona como esperado.
        """
        response = self.client.post(self.record_attendance_url, self.record_attendance_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AttendanceRecord.objects.count(), 2)
        self.assertTrue(AttendanceRecord.objects.filter(student=self.student1, attending=True).exists())

    def test_view_attendance(self):
        """
        Testa se a API de visualizar presença retorna os dados esperados.
        """
        # Primeiro, registra a presença para ter dados para visualizar
        self.client.post(self.record_attendance_url, self.record_attendance_data, format='json')

        # Construir a URL para visualizar a presença com os parâmetros desejados
        response = self.client.get(f"{self.view_attendance_url}?period=afternoon&schoolGrade=6&date=2023-10-12")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Deve retornar a presença de dois alunos
        self.assertTrue(all(item['attending'] == True for item in response.data))  # Verifica se todos estão presentes
