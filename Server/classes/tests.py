from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from users.models import Teacher
from classes.models import Class
from attendance_app.models import Student, Statistics
from rest_framework_simplejwt.tokens import RefreshToken

from classes.models import Subject


class ClassActionTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.teacher_password = "testpassword123"
        self.teacher = Teacher.objects.create_user(
            username="teacher1",
            password=self.teacher_password,
            name="Teacher One",
            role="Teacher"
        )

        # Create tokens
        refresh = RefreshToken.for_user(self.teacher)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        self.class_instance = Class.objects.create(
            period="Morning",
            schoolGrade=1,
            classMeta="Math",
            teacher=self.teacher
        )

        # Adicionando estudantes e estatísticas para testar
        self.student1 = Student.objects.create(name="Student One")
        self.student2 = Student.objects.create(name="Student Two")
        self.class_instance.students.add(self.student1, self.student2)

        self.statistics1 = Statistics.objects.create(student=self.student1, classMeta=self.class_instance,
                                                     total_classes=10, attended_classes=8)
        self.statistics2 = Statistics.objects.create(student=self.student2, classMeta=self.class_instance,
                                                     total_classes=10, attended_classes=6)

    def test_choose_action_valid_token(self):
        url = reverse('class-actions', args=[self.class_instance.id])

        # Testar a ação "Fazer Chamada"
        data = {"action": "Fazer Chamada"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Verifica se há dois alunos na lista
        self.assertEqual(response.data[0]['name'], "Student One")
        self.assertEqual(response.data[1]['name'], "Student Two")

        # Testar a ação "Verificar Estatísticas"
        data = {"action": "Verificar Estatísticas"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Verifica se há duas estatísticas na lista
        self.assertEqual(response.data[0]['student'], self.student1.id)
        self.assertEqual(response.data[1]['student'], self.student2.id)
        self.assertEqual(response.data[0]['attendance_percentage'], 80.0)
        self.assertEqual(response.data[1]['attendance_percentage'], 60.0)

        # Testar a ação "Ver Lista de Alunos"
        data = {"action": "Ver Lista de Alunos"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Verifica se há dois alunos na lista
        self.assertEqual(response.data[0]['name'], "Student One")
        self.assertEqual(response.data[1]['name'], "Student Two")

    def test_choose_action_invalid_token(self):
        self.client.credentials()  # Remove o token de autenticação
        url = reverse('class-actions', args=[self.class_instance.id])
        data = {"action": "Fazer Chamada"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ClassSelectionTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.teacher_password = "testpassword123"
        self.teacher = Teacher.objects.create_user(
            username="teacher1",
            password=self.teacher_password,
            name="Teacher One",
            role="Teacher"
        )

        # Create tokens
        refresh = RefreshToken.for_user(self.teacher)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        self.class_instance = Class.objects.create(
            period="Morning",
            schoolGrade=1,
            classMeta="Math",
            teacher=self.teacher
        )

    def test_list_classes_valid_token(self):
        url = reverse('class-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Verifica se há uma classe na lista

    def test_list_classes_invalid_token(self):
        self.client.credentials()  # Remove o token de autenticação
        url = reverse('class-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class StudentListViewTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.teacher_password = "testpassword123"
        self.teacher = Teacher.objects.create_user(
            username="teacher1",
            password=self.teacher_password,
            name="Teacher One",
            role="Teacher"
        )

        # Create tokens
        refresh = RefreshToken.for_user(self.teacher)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        self.class_instance = Class.objects.create(
            period="Morning",
            schoolGrade=1,
            classMeta="Math",
            teacher=self.teacher
        )

        self.student1 = Student.objects.create(name="Student One")
        self.student2 = Student.objects.create(name="Student Two")
        self.class_instance.students.add(self.student1, self.student2)

    def test_view_student_list_valid_token(self):
        url = reverse('student-list', args=[self.class_instance.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Verifica se há dois alunos na lista
        self.assertEqual(response.data[0]['name'], "Student One")
        self.assertEqual(response.data[1]['name'], "Student Two")

    def test_view_student_list_invalid_token(self):
        self.client.credentials()  # Remove o token de autenticação
        url = reverse('student-list', args=[self.class_instance.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class StudentSubjectListViewTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.teacher_password = "testpassword123"
        self.teacher = Teacher.objects.create_user(
            username="teacher1",
            password=self.teacher_password,
            name="Teacher One",
            role="Teacher"
        )

        # Create tokens
        refresh = RefreshToken.for_user(self.teacher)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        self.class_instance = Class.objects.create(
            period="Morning",
            schoolGrade=1,
            classMeta="Math",
            teacher=self.teacher
        )

        self.student1 = Student.objects.create(name="Student One")
        self.student2 = Student.objects.create(name="Student Two")
        self.class_instance.students.add(self.student1, self.student2)

        self.subject1 = Subject.objects.create(name="Math", classMeta=self.class_instance)
        self.subject1.students.add(self.student1, self.student2)

    def test_view_student_subjects_valid_token(self):
        url = reverse('student-subject-list', args=[self.student1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Verifica se há um sujeito na lista
        self.assertEqual(response.data[0]['name'], "Math")

    def test_view_student_subjects_invalid_token(self):
        self.client.credentials()  # Remove o token de autenticação
        url = reverse('student-subject-list', args=[self.student1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
