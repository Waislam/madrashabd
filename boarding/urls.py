from django.urls import path
from .views import BazarListView

urlpatterns = [
    path('bazarlist/', BazarListView.as_view()),
]