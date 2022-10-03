from django.urls import path
from .views import BazarListView

urlpatterns = [
    path('bazarlist/<slug:slug>/', BazarListView.as_view()),
]