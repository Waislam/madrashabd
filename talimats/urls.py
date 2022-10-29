from django.urls import path
from .views import (
    BookDistributionToTeacherView,
    BookDistToTeacherDetailView
)

urlpatterns = [
    path('<madrasha_slug>/book-dist-teacher/', BookDistributionToTeacherView.as_view()),
    path('book-dist-teacher/detail/<int:pk>/', BookDistToTeacherDetailView.as_view()),
]
