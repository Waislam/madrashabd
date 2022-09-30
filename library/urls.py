from django.urls import path
from library import views

urlpatterns = [
    path('', views.LibaryBookView.as_view()),
    path('detail/<int:pk>/', views.BookDetailView.as_view()),
]