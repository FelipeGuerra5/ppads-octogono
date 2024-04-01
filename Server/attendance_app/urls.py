from django.urls import path
from .views import ListStudentsView, RecordAttendanceView

urlpatterns = [
    path('listStudents/', ListStudentsView.as_view(), name='list-students'),
    path('recordAttendance/', RecordAttendanceView.as_view(), name='record-attendance'),
]
