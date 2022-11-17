from django.shortcuts import render
from rest_framework import mixins, generics

from darul_ekama.models import SeatBooking, NigraniTable
from darul_ekama.serializers import (SeatBookingSerializer,
                                     SeatBookingListSerializer,
                                     NigraniTableListSerializer,
                                     NigraniTableSerializer,

                                     )
from students.models import Student


# Create your views here.
class SeatBookingView(mixins.CreateModelMixin,
                      mixins.ListModelMixin, generics.GenericAPIView
                      ):
    queryset = SeatBooking.objects.all()

    # serializer_class = SeatBookingSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SeatBookingListSerializer
        return SeatBookingSerializer

    def get_queryset(self):
        madrsha_slug = self.kwargs['madrasha_slug']
        queryset = super(SeatBookingView, self).get_queryset().filter(madrasha__slug=madrsha_slug)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        student_id = request.data['students']
        student = Student.objects.get(student_id=student_id)
        request.data['students'] = student.id
        return self.create(request, *args, **kwargs)


class NigraniTableView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = NigraniTable.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return NigraniTableListSerializer
        return NigraniTableSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


