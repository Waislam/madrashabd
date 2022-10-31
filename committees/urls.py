
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.CommitteeListView.as_view()),
    path('details/<int:pk>/', views.CommitteeDetail.as_view()),
]