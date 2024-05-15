from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from users.models import Teacher


class UserLoginTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.teacher_password = "testpassword123"
        self.teacher = Teacher.objects.create_user(
            username="teacher1",
            password=self.teacher_password,
            name="Teacher One",
            role="Teacher"
        )
        self.parent_password = "testpassword456"
        self.parent = Teacher.objects.create_user(
            username="parent1",
            password=self.parent_password,
            name="Parent One",
            role="Parent"
        )

    def test_login_teacher_valid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': self.teacher.username,
            'password': self.teacher_password
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Login successful', response.data['message'])

    def test_login_parent_valid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': self.parent.username,
            'password': self.parent_password
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Login successful', response.data['message'])

    def test_login_invalid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': self.teacher.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Invalid credentials', response.data['message'])
