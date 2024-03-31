from django.db import models
from django.utils import timezone


class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Class(models.Model):
    period = models.CharField(max_length=50)
    schoolGrade = models.IntegerField()
    classMeta = models.CharField(max_length=100, db_column='class')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('period', 'schoolGrade', 'classMeta', 'teacher')

    def __str__(self):
        return f"{self.classMeta} - Grade {self.schoolGrade} - {self.period}"



class AttendanceRecord(models.Model):
    classMeta = models.ForeignKey(Class, related_name='attendance_records', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attending = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.student.name} - {'Present' if self.attending else 'Absent'} on {self.date}"
