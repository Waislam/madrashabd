from django.urls import path
from .views import StudentView, StudentDetailView

urlpatterns = [
    path('<int:madrasha_slug>/', StudentView.as_view()),
    path('detail/<slug:slug>/', StudentDetailView.as_view()),
]