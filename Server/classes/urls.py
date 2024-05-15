from django.urls import path
from .views import ClassListView, ClassActionView, StudentListView, StudentSubjectListView

urlpatterns = [
    path('', ClassListView.as_view(), name='class-list'),
    path('<int:class_id>/actions/', ClassActionView.as_view(), name='class-actions'),
    path('<int:class_id>/students/', StudentListView.as_view(), name='student-list'),
    path('<int:student_id>/subjects/', StudentSubjectListView.as_view(), name='student-subject-list'),
]
