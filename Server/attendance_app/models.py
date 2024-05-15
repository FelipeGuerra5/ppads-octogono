from django.db import models
from django.utils import timezone

from classes.models import Class, Student


class AttendanceRecord(models.Model):
    classMeta = models.ForeignKey(Class, related_name='attendance_records', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attending = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.student.name} - {'Present' if self.attending else 'Absent'} on {self.date}"

class Statistics(models.Model):
    student = models.ForeignKey('classes.Student', on_delete=models.CASCADE)
    classMeta = models.ForeignKey('classes.Class', on_delete=models.CASCADE)
    total_classes = models.IntegerField(default=0)
    attended_classes = models.IntegerField(default=0)

    @property
    def attendance_percentage(self):
        if self.total_classes > 0:
            return (self.attended_classes / self.total_classes) * 100
        return 0

    def __str__(self):
        return f"{self.student.name} - {self.classMeta.classMeta} - {self.attendance_percentage}%"
