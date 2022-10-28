"""
1. Book Distribtuion to teacher view
"""
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import mixins, generics, status
from talimats.models import BookDistributeToTeacher
from rest_framework.response import Response
from talimats.serializers import (
    BookDistributionToTeacherSerializer
)
from talimats.serializers import (
    BookDistributionToTeacherListSerializer
)


# Create your views here.

# ====================== 1. Book Distribtuion to teacher view ================
class BookDistributionToTeacherView(mixins.CreateModelMixin,
                                    mixins.ListModelMixin,
                                    generics.GenericAPIView
                                    ):
    queryset = BookDistributeToTeacher.objects.all()

    def get_queryset(self):
        madrasha_slug = self.kwargs['madrasha_slug']
        return super(BookDistributionToTeacherView, self).get_queryset().filter(madrasha__slug=madrasha_slug)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BookDistributionToTeacherListSerializer
        return BookDistributionToTeacherSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookDistToTeacherDetailView(APIView):

    def get_object(self, pk):
        try:
            return BookDistributeToTeacher.objects.get(id=pk)
        except BookDistributeToTeacher.DoesNotExist:
            raise Http404

    def get(self, request, pk, formate=None):
        obj = self.get_object(pk)
        serializer = BookDistributionToTeacherListSerializer(obj)
        return Response({"status": True, "data": serializer.data})

    def put(self, request, pk, formate=None):
        obj = self.get_object(pk)
        serializer = BookDistributionToTeacherSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "message": "Book Distribtuion to teacher has been updated successfully",
                    "data": serializer.data,
                }
            )
        return Response({"status": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)





