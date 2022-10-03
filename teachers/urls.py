from django.urls import path
from .views import TeacherView, TeacherDetailView

urlpatterns = [
    path('', TeacherView.as_view()),
    path('detail/<slug:slug>/', TeacherDetailView.as_view()),
]