from django.db import models

from accounts.models import Madrasha
from settingapp.models import Building, Room, Seat
from students.models import Student


# Create your models here.

class SeatBooking(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT, related_name='madrasha_seat_booking')
    students = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='student_seat_dist')
    building = models.ForeignKey(Building, on_delete=models.SET_NULL, related_name='building_seats', blank=True, null=True)
    floor = models.CharField(max_length=3)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, related_name='room_seats', blank=True, null=True)
    seat = models.ForeignKey(Seat, on_delete=models.SET_NULL, related_name='booked_seat', blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.seat.seat_number)

