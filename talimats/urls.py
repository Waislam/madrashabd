from django.urls import path
from .views import (
    BookDistributionToTeacherView,
    BookDistToTeacherDetailView,
    TeacherTrainingView,
    TeacherTrainingDetailView,
    SyllabusView,
    SyllabusDetailView,
    ExamAnnouncementView,
    ExamAnnouncementDetailView,
    ExamRegistrationListView,
    ExamTermListView,
    HallDutyListView,
    HallNigranDetailView
)

urlpatterns = [
    path('<madrasha_slug>/book-dist-teacher/', BookDistributionToTeacherView.as_view()),
    path('book-dist-teacher/detail/<int:pk>/', BookDistToTeacherDetailView.as_view()),

    path('<madrasha_slug>/teacher-training/', TeacherTrainingView.as_view()),
    path('teacher-training/detail/<int:pk>/', TeacherTrainingDetailView.as_view()),

    path('<madrasha_slug>/syllabus/', SyllabusView.as_view()),
    path('syllabus/detail/<int:pk>/', SyllabusDetailView.as_view()),

    path('<madrasha_slug>/exam-announcement/', ExamAnnouncementView.as_view()),
    path('exam-announcement/detail/<int:pk>/', ExamAnnouncementDetailView.as_view()),

    path('<madrasha_slug>/exam-registration/', ExamRegistrationListView.as_view()),

    path('<madrasha_slug>/exam-term/', ExamTermListView.as_view()),

    path('<madrasha_slug>/hall-duty/', HallDutyListView.as_view()),
    path('hall-duty/detail/<int:pk>/', HallNigranDetailView.as_view()),
]
