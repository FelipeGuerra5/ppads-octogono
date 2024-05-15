from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from users.models import Teacher
from classes.models import Class, Student
from attendance_app.models import AttendanceRecord

from attendance_app.models import Statistics


class AttendanceRecordTests(TestCase):

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

    def test_attendance_record_valid_token(self):
        url = reverse('class-attendance')
        data = {
            "period": "Morning",
            "schoolGrade": 1,
            "classMeta": "Math",
            "teacher": self.teacher.id,
            "date": "2024-05-15",
            "studentsList": [
                {"student": self.student1.id, "attending": True},
                {"student": self.student2.id, "attending": False}
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AttendanceRecord.objects.count(), 2)
        self.assertEqual(AttendanceRecord.objects.get(student=self.student1).attending, True)
        self.assertEqual(AttendanceRecord.objects.get(student=self.student2).attending, False)

    def test_attendance_record_invalid_token(self):
        self.client.logout()
        url = reverse('class-attendance')
        data = {
            "period": "Morning",
            "schoolGrade": 1,
            "classMeta": "Math",
            "teacher": self.teacher.id,
            "date": "2024-05-15",
            "studentsList": [
                {"student": self.student1.id, "attending": True},
                {"student": self.student2.id, "attending": False}
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_attendance_record_invalid_data(self):
        url = reverse('class-attendance')
        data = {
            "period": "Morning",
            "schoolGrade": 1,
            "classMeta": "Math",
            "teacher": self.teacher.id,
            "date": "invalid-date",
            "studentsList": [
                {"student": self.student1.id, "attending": True},
                {"student": self.student2.id, "attending": False}
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class StatisticsTests(TestCase):

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

        AttendanceRecord.objects.create(classMeta=self.class_instance, student=self.student1, attending=True, date="2024-05-01")
        AttendanceRecord.objects.create(classMeta=self.class_instance, student=self.student1, attending=True, date="2024-05-02")
        AttendanceRecord.objects.create(classMeta=self.class_instance, student=self.student2, attending=False, date="2024-05-01")
        AttendanceRecord.objects.create(classMeta=self.class_instance, student=self.student2, attending=True, date="2024-05-02")

        Statistics.objects.create(student=self.student1, classMeta=self.class_instance, total_classes=2, attended_classes=2)
        Statistics.objects.create(student=self.student2, classMeta=self.class_instance, total_classes=2, attended_classes=1)

    def test_view_statistics_valid_token(self):
        url = reverse('class-statistics', args=[self.class_instance.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['student'], self.student1.id)
        self.assertEqual(response.data[0]['attendance_percentage'], 100.0)
        self.assertEqual(response.data[1]['student'], self.student2.id)
        self.assertEqual(response.data[1]['attendance_percentage'], 50.0)

    def test_view_statistics_invalid_token(self):
        self.client.logout()
        url = reverse('class-statistics', args=[self.class_instance.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class StudentStatisticsViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.teacher_password = "testpassword123"
        self.parent_password = "testpassword456"

        self.teacher = Teacher.objects.create_user(
            username="teacher1",
            password=self.teacher_password,
            name="Teacher One",
            role="Teacher"
        )
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
            teacher=self.teacher
        )

        self.student = Student.objects.create(name="Student One", parent=self.parent)
        self.class_instance.students.add(self.student)

        AttendanceRecord.objects.create(classMeta=self.class_instance, student=self.student, attending=True,
                                        date="2024-05-01")
        AttendanceRecord.objects.create(classMeta=self.class_instance, student=self.student, attending=True,
                                        date="2024-05-02")

        Statistics.objects.create(student=self.student, classMeta=self.class_instance, total_classes=2,
                                  attended_classes=2)

    def test_view_student_statistics_teacher_valid_token(self):
        self.client.login(username=self.teacher.username, password=self.teacher_password)
        url = reverse('student-statistics', args=[self.student.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        statistics = response.data[0]
        self.assertEqual(statistics['student'], self.student.id)
        self.assertEqual(statistics['attendance_percentage'], 100.0)

    def test_view_student_statistics_parent_valid_token(self):
        self.client.login(username=self.parent.username, password=self.parent_password)
        url = reverse('student-statistics', args=[self.student.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        statistics = response.data[0]
        self.assertEqual(statistics['student'], self.student.id)
        self.assertEqual(statistics['attendance_percentage'], 100.0)

    def test_view_student_statistics_invalid_token(self):
        self.client.logout()  # Invalidate the token by logging out
        url = reverse('student-statistics', args=[self.student.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
