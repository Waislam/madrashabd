from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework import status
from .models import Student
from .pagination import CustomPagination


# Create your views here.


class StudentView(APIView, CustomPagination):
    """ Student Create and list view """
    def get(self, request, formate=None):
        """method to show the list of Students """
        students = Student.objects.all()
        result = self.paginate_queryset(students, request, view=self)
        serializer = StudentSerializer(result, many=True)
        # return Response({'status': True, 'data': serializer.data})
        return self.get_paginated_response(serializer.data)

    def post(self, request, formate=None):
        """Method to create student api """
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': 'Student has been created'})
        return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


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



