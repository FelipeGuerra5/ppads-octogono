from django.db import models
from users.models import Teacher  # Corrigida a importação

class Student(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Teacher, related_name='children', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Class(models.Model):
    period = models.CharField(max_length=50)
    schoolGrade = models.IntegerField()
    classMeta = models.CharField(max_length=100, db_column='class')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='classes')

    class Meta:
        unique_together = ('period', 'schoolGrade', 'classMeta', 'teacher')

    def __str__(self):
        return f"{self.classMeta} - Grade {self.schoolGrade} - {self.period}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    classMeta = models.ForeignKey(Class, related_name='subjects', on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='subjects')

    def __str__(self):
        return self.name
