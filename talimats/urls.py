from django.urls import path
from .views import (
    BookDistributionToTeacherView,
    BookDistToTeacherDetailView,
    TeacherTrainingView,
    TeacherTrainingDetailView,
    SyllabusView,
    SyllabusDetailView,
    TeacherStaffResponsibilityDetailView,
    TeacherStaffResponsibilityView
)

urlpatterns = [
    path('<madrasha_slug>/book-dist-teacher/', BookDistributionToTeacherView.as_view()),
    path('book-dist-teacher/detail/<int:pk>/', BookDistToTeacherDetailView.as_view()),

    path('<madrasha_slug>/teacher-training/', TeacherTrainingView.as_view()),
    path('teacher-training/detail/<int:pk>/', TeacherTrainingDetailView.as_view()),

    path('<madrasha_slug>/syllabus/', SyllabusView.as_view()),
    path('syllabus/detail/<int:pk>/', SyllabusDetailView.as_view()),

    path('<madrasha_slug>/responsibility/', TeacherStaffResponsibilityView.as_view()),
    path('responsibility/detail/<int:pk>/', TeacherStaffResponsibilityDetailView.as_view()),
]
