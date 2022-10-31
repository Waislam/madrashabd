"""
1. Book Distribution to teacher view
2. Teacher Training View
3. Syllabus View
"""
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins, generics, status
from talimats.models import (
    BookDistributeToTeacher,
    TeacherTraining,
    Syllabus,
    Dawah,
    ExtraActivity
)

from rest_framework.response import Response
from talimats.serializers import (
    BookDistributionToTeacherSerializer,
    TeacherTrainingSerializer,
    SyllabusSerializer,
    SyllabusListSerializer,
    DawahSerializer,
    ExtraActivityListSerializer

)
from talimats.serializers import (
    BookDistributionToTeacherListSerializer,
    TeacherTrainingListSerializer,
    DawahListSerializer,
    ExtraActivitySerializer
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


# ====================== 16. Dawah view ================
class DawahView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    queryset = Dawah.objects.all()

    def get_queryset(self):
        madrasha_slug = self.kwargs['madrasha_slug']
        return super(DawahView, self).get_queryset().filter(madrasha__slug=madrasha_slug)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DawahListSerializer
        return DawahSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DawahDetailView(APIView):

    def get_object(self, pk):
        try:
            return Dawah.objects.get(id=pk)
        except Dawah.DoesNotExist:
            raise Http404

    def get(self, request, pk, formate=None):
        obj = self.get_object(pk)
        serializer = DawahListSerializer(obj)
        return Response({"status": True, "data": serializer.data})

    def put(self, request, pk, formate=None):
        obj = self.get_object(pk)
        serializer = DawahSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "message": "Dawah has been updated successfully",
                    "data": serializer.data,
                }
            )
        return Response({"status": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, formate=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(
            {
                "status": True,
                "message": "Dawah has been successfully Delete",
            }
        )


# ====================== 17. ExtraActivity View ================
class ExtraActivityView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    queryset = ExtraActivity.objects.all()

    def get_queryset(self):
        madrasha_slug = self.kwargs['madrasha_slug']
        return super(ExtraActivityView, self).get_queryset().filter(madrasha__slug=madrasha_slug)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ExtraActivityListSerializer
        return ExtraActivitySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ExtraActivityDetailView(APIView):

    def get_object(self, pk):
        try:
            return ExtraActivity.objects.get(id=pk)
        except ExtraActivity.DoesNotExist:
            raise Http404

    def get(self, request, pk, formate=None):
        obj = self.get_object(pk)
        serializer = ExtraActivityListSerializer(obj)
        return Response({"status": True, "data": serializer.data})

    def put(self, request, pk, formate=None):
        obj = self.get_object(pk)
        serializer = ExtraActivitySerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "message": "Extra Activity has been updated successfully",
                    "data": serializer.data,
                }
            )
        return Response({"status": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, formate=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(
            {
                "status": True,
                "message": "Extra activity has been successfully Delete",
            }
        )
