from django.urls import path
from darul_ekama.views import SeatBookingView

urlpatterns = [
    path('<madrasha_slug>/seat-booking/', SeatBookingView.as_view()),
]