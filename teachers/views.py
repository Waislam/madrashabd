from django.shortcuts import render
from django.http import Http404
from .serializers import TeacherSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher
from students.pagination import CustomPagination

# Create your views here.


class TeacherView(APIView, CustomPagination):
    """to create and list teacher obj"""
    def get(self, request, formate=None):
        """get list of teachers"""
        teachers = Teacher.objects.all()
        result = self.paginate_queryset(teachers, request, view=self)
        serializer = TeacherSerializer(result, many=True)
        # return Response({'status': True, 'data': serializer.data})
        return self.get_paginated_response(serializer.data)

    def post(self, request, formate=None):
        """to create teacher obj"""
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'data': serializer.data})
        return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetailView(APIView):
    """ put, get, no delete"""
    def get_object(self, slug):
        """get single obj"""
        try:
            return Teacher.objects.get(slug=slug)
        except Teacher.DoesNotExist:
            raise Http404

    def get(self, request, slug, formate=None):
        """veiw details of single obj"""
        teacher = self.get_object(slug)
        serializer = TeacherSerializer(teacher)
        return Response({'status': True, 'data': serializer.data})

    def put(self, request, slug, formate=None):
        """update single teacher"""
        teacher = self.get_object(slug)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'data': serializer.data})
        return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)