from django.urls import path
from .views import ClassAttendanceView, ClassStatisticsView, StudentStatisticsView, AttendanceRecordView

urlpatterns = [
    path('<int:class_id>/attendance/', ClassAttendanceView.as_view(), name='class-attendance'),
    path('<int:class_id>/statistics/', ClassStatisticsView.as_view(), name='class-statistics'),
    path('student/<int:student_id>/statistics/', StudentStatisticsView.as_view(), name='student-statistics'),
    path('attendance-records/', AttendanceRecordView.as_view(), name='attendance-records'),
]
