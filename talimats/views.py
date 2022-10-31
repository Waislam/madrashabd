"""
1. Book Distribution to teacher view
2. Teacher Training View
3. Syllabus View
4. TeacherStaffResponsibility View
"""
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins, generics, status
from talimats.models import BookDistributeToTeacher, TeacherTraining, Syllabus, TeacherStaffResponsibility
from rest_framework.response import Response
from talimats.serializers import (
    BookDistributionToTeacherSerializer,
    TeacherTrainingSerializer, SyllabusSerializer,
    TeacherStaffResponsibilitySerializer
)
from talimats.serializers import (
    BookDistributionToTeacherListSerializer,
    TeacherTrainingListSerializer,
    SyllabusListSerializer,
    TeacherStaffResponsibilityListSerializer
)


# Create your views here.

# ====================== 1. Book Distribution to teacher view ================
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


# ====================== 2. Teacher Training View ================
class TeacherTrainingView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    queryset = TeacherTraining.objects.all()

    def get_queryset(self):
        madrasha_slug = self.kwargs['madrasha_slug']
        queryset = super().get_queryset().filter(madrasha__slug=madrasha_slug)
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return TeacherTrainingListSerializer
        return TeacherTrainingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TeacherTrainingDetailView(APIView):
    def get_object(self, pk):
        try:
            return TeacherTraining.objects.get(id=pk)
        except TeacherTraining.DoesNotExist:
            return Http404

    def get(self, request, pk, formate=None):
        obj = self.get_object(pk)
        serializer = TeacherTrainingListSerializer(obj)
        return Response({"status": True, "data": serializer.data})

    def put(self, request, pk, formate=None):
        obj = self.get_object(pk)
        serializer = TeacherTrainingSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "message": "Teacher Training notice has been updated successfully",
                    "data": serializer.data,
                }
            )
        return Response({"status": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# ====================== 3. Syllabus View ================
class SyllabusView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    queryset = Syllabus.objects.all()

    def get_queryset(self):
        madrasha_slug = self.kwargs['madrasha_slug']
        queryset = super().get_queryset().filter(madrasha__slug=madrasha_slug)
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SyllabusListSerializer
        return SyllabusSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SyllabusDetailView(APIView):
    def get_object(self, pk):
        try:
            return Syllabus.objects.get(id=pk)
        except Syllabus.DoesNotExist:
            return Http404

    def get(self, request, pk, formate=None):
        obj = self.get_object(pk)
        serializer = SyllabusListSerializer(obj)
        return Response({"status": True, "data": serializer.data})

    def put(self, request, pk, formate=None):
        obj = self.get_object(pk)
        serializer = SyllabusSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "message": "Syllabus has been updated successfully",
                    "data": serializer.data,
                }
            )
        return Response({"status": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# ====================== 4. TeacherStaffResponsibility View ================
class TeacherStaffResponsibilityView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    queryset = TeacherStaffResponsibility.objects.all()

    def get_queryset(self):
        madrasha_slug = self.kwargs['madrasha_slug']
        queryset = super().get_queryset().filter(madrasha__slug=madrasha_slug)
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return TeacherStaffResponsibilityListSerializer
        return TeacherStaffResponsibilitySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TeacherStaffResponsibilityDetailView(APIView):
    def get_object(self, pk):
        try:
            return TeacherStaffResponsibility.objects.get(id=pk)
        except TeacherStaffResponsibility.DoesNotExist:
            return Http404

    def get(self, request, pk, formate=None):
        obj = self.get_object(pk)
        serializer = TeacherStaffResponsibilityListSerializer(obj)
        return Response({"status": True, "data": serializer.data})

    def put(self, request, pk, formate=None):
        obj = self.get_object(pk)
        serializer = TeacherStaffResponsibilitySerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "message": "Object has been updated successfully",
                    "data": serializer.data,
                }
            )
        return Response({"status": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
