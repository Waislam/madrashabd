from django.urls import path
from . import views

urlpatterns = [

    path('<madrasha_slug>/vehicle-info-list/', views.VehicleInfoListView.as_view()),
    path('vehicle-info/details/<int:pk>/', views.VehicleInfoDetail.as_view()),

    path('<madrasha_slug>/transport-list/', views.TransportDetailListView.as_view()),
    path('transport/details/<int:pk>/', views.TransportDetailView.as_view()),
]
