from django.urls import path
from .views import StudentView, StudentDetailView, CheckUniquePassportNumber, CheckUniqueNIDNumber

urlpatterns = [
    path('', StudentView.as_view()),
    path('detail/<slug:slug>/', StudentDetailView.as_view()),
    path('check-passport/<str:passport_number>/', CheckUniquePassportNumber.as_view()),
    path('check-nid/<str:nid_number>/', CheckUniqueNIDNumber.as_view()),
]