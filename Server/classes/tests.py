from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from users.models import Teacher
from classes.models import Class

from classes.models import Student

from classes.models import Subject


class ClassSelectionTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.teacher_password = "testpassword123"
        self.teacher = Teacher.objects.create_user(
            username="teacher1",
            password=self.teacher_password,
            name="Teacher One",
            role="Teacher"
        )
        self.client.login(username=self.teacher.username, password=self.teacher_password)

        self.class1 = Class.objects.create(
            period="Morning",
            schoolGrade=1,
            classMeta="Math",
            teacher=self.teacher
        )

        self.class2 = Class.objects.create(
            period="Afternoon",
            schoolGrade=2,
            classMeta="Science",
            teacher=self.teacher
        )

    def test_list_classes_valid_token(self):
        response = self.client.get(reverse('class-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['classMeta'], 'Math')
        self.assertEqual(response.data[1]['classMeta'], 'Science')

    def test_list_classes_invalid_token(self):
        self.client.logout()
        response = self.client.get(reverse('class-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ClassActionTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.teacher_password = "testpassword123"
        self.teacher = Teacher.objects.create_user(
            username="teacher1",
            password=self.teacher_password,
            name="Teacher One",
            role="Teacher"
        )
        self.client.login(username=self.teacher.username, password=self.teacher_password)

        self.class_instance = Class.objects.create(
            period="Morning",
            schoolGrade=1,
            classMeta="Math",
            teacher=self.teacher
        )

    def test_choose_action_valid_token(self):
        url = reverse('class-actions', args=[self.class_instance.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Fazer Chamada", response.data['actions'])
        self.assertIn("Verificar Estatísticas", response.data['actions'])
        self.assertIn("Ver Lista de Alunos", response.data['actions'])

    def test_choose_action_invalid_token(self):
        self.client.logout()
        url = reverse('class-actions', args=[self.class_instance.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class StudentListViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.teacher_password = "testpassword123"
        self.teacher = Teacher.objects.create_user(
            username="teacher1",
            password=self.teacher_password,
            name="Teacher One",
            role="Teacher"
        )
        self.client.login(username=self.teacher.username, password=self.teacher_password)

        self.class_instance = Class.objects.create(
            period="Morning",
            schoolGrade=1,
            classMeta="Math",
            teacher=self.teacher
        )

        self.student1 = Student.objects.create(name="Student One", parent=self.teacher)
        self.student2 = Student.objects.create(name="Student Two", parent=self.teacher)

        self.class_instance.students.add(self.student1, self.student2)

    def test_view_student_list_valid_token(self):
        url = reverse('student-list', args=[self.class_instance.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Student One')
        self.assertEqual(response.data[1]['name'], 'Student Two')

    def test_view_student_list_invalid_token(self):
        self.client.logout()
        url = reverse('student-list', args=[self.class_instance.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class StudentSubjectListViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.parent_password = "testpassword456"

        self.parent = Teacher.objects.create_user(
            username="parent1",
            password=self.parent_password,
            name="Parent One",
            role="Parent"
        )

        self.class_instance = Class.objects.create(
            period="Morning",
            schoolGrade=1,
            classMeta="Math",
            teacher=self.parent
        )

        self.student = Student.objects.create(name="Student One", parent=self.parent)
        self.class_instance.students.add(self.student)

        self.subject1 = Subject.objects.create(name="Math", classMeta=self.class_instance)
        self.subject2 = Subject.objects.create(name="Science", classMeta=self.class_instance)

        self.subject1.students.add(self.student)
        self.subject2.students.add(self.student)

    def test_view_student_subjects_valid_token(self):
        self.client.login(username=self.parent.username, password=self.parent_password)
        url = reverse('student-subject-list', args=[self.student.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Math')
        self.assertEqual(response.data[1]['name'], 'Science')

    def test_view_student_subjects_invalid_token(self):
        self.client.logout()
        url = reverse('student-subject-list', args=[self.student.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
