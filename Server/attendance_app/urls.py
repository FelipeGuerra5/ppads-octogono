from django.urls import path
from .views import ClassAttendanceView, AttendanceRecordView

urlpatterns = [
    path('register-attendance/', ClassAttendanceView.as_view(), name='register_attendance'),
    path('view-attendance/', AttendanceRecordView.as_view(), name='view-attendance'),
]
