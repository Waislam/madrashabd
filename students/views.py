from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework import status
from .models import Student
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import StudentFilter


# Create your views here.

class StudentView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """ Student Create and list view """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StudentFilter
    search_fields = ['student_id']

    def get(self, request, *args, **kwargs):
        """method to show the list of Students """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Method to create student obj """
        return self.create(request, *args, **kwargs)


class StudentDetailView(APIView):
    """ this class is for CRUD"""

    def get_object(self, slug):
        """For getting single obj with slug field"""
        try:
            return Student.objects.get(slug=slug)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, slug, formate=None):
        """For getting single student details"""
        student = self.get_object(slug)
        serializer = StudentSerializer(student)
        return Response({'status': True, 'data': serializer.data})

    def put(self, request, slug, formate=None):
        """update single obj details"""
        student = self.get_object(slug)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': 'student profile has been updated successfully','data': serializer.data})
        return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



