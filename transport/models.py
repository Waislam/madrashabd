from django.db import models
from accounts.models import Madrasha
from students.models import Student


class VehicleInfo(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.CASCADE, blank=True, null=True)
    car_number = models.CharField(max_length=250)
    driver_name = models.CharField(max_length=250)
    driver_number = models.CharField(max_length=20)
    route = models.CharField(max_length=250)
    time = models.TimeField()

    def __str__(self):
        return self.driver_name


class TransportDetail(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.CASCADE, blank=True, null=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    vehicle = models.ForeignKey(VehicleInfo, on_delete=models.CASCADE, blank=True, null=True)
    start_time = models.TimeField()

    def __str__(self):
        return str(self.id)
