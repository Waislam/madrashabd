from django.urls import path
from .views import BazarListView

urlpatterns = [
    path('bazarlist/<madrasha_slug>/', BazarListView.as_view()),
]