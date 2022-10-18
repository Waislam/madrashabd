from django.urls import path
from library import views

urlpatterns = [
    path('<int:madrasha_slug>/', views.LibaryBookView.as_view()),
    path('detail/<int:pk>/', views.BookDetailView.as_view()),
    path('<int:madrasha_slug>/book-distribution/', views.BookDistributionListView.as_view()),
    path('book-distribution/delete/<int:pk>/', views.BookDistributionDelete.as_view()),
]