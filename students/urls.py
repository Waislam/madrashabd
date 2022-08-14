from django.urls import path
from .views import StudentView, StudentDetailView

urlpatterns = [
    path('', StudentView.as_view()),
    path('detail/<slug:slug>/', StudentDetailView.as_view()),
]