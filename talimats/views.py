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
    ExamAnnouncement,
    ExamRegistration,
    ExamTerm,
    HallDuty
)
from rest_framework.response import Response
from talimats.serializers import (
    BookDistributionToTeacherSerializer,
    TeacherTrainingSerializer,
    SyllabusSerializer,
    SyllabusListSerializer,
    ExamAnnouncementListSerializer,
    ExamAnnouncementSerializer,
    ExamRegistrationListSerializer,
    ExamRegistrationSerializer,
    ExamTermSerializer,
    HallDutySerializer
)
from talimats.serializers import (
    BookDistributionToTeacherListSerializer,
    TeacherTrainingListSerializer
)
from core.pagination import CustomPagination


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


class ExamAnnouncementView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = ExamAnnouncement.objects.all()
    pagination_class = CustomPagination

    def get_queryset(self):
        madrasha_slug = self.kwargs['madrasha_slug']
        queryset = super().get_queryset().filter(madrasha__slug=madrasha_slug)
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ExamAnnouncementListSerializer
        return ExamAnnouncementSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ExamAnnouncementDetailView(APIView):

    def get_object(self, pk):
        try:
            return ExamAnnouncement.objects.get(id=pk)
        except ExamAnnouncement.DoesNotExist:
            return Http404

    def get(self, request, pk, formate=None):
        obj = self.get_object(pk)
        serializer = ExamAnnouncementListSerializer(obj)
        return Response({"status": True, "data": serializer.data})

    def put(self, request, pk, formate=None):
        obj = self.get_object(pk)
        serializer = ExamAnnouncementSerializer(obj, data=request.data)
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

    def delete(self, request, pk, format=None):
        exam_announcement = self.get_object(pk)
        exam_announcement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExamRegistrationListView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    queryset = ExamRegistration.objects.all()
    pagination_class = CustomPagination

    def get_queryset(self):
        madrasha_slug = self.kwargs['madrasha_slug']
        queryset = super().get_queryset().filter(madrasha__slug=madrasha_slug)
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ExamRegistrationListSerializer
        return ExamRegistrationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ExamTermListView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    queryset = ExamTerm.objects.all()

    def get_queryset(self):
        madrasha_slug = self.kwargs['madrasha_slug']
        queryset = super().get_queryset().filter(madrasha__slug=madrasha_slug)
        return queryset

    def get_serializer_class(self):
        return ExamTermSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class HallDutyListView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    queryset = HallDuty.objects.all()

    def get_queryset(self):
        madrasha_slug = self.kwargs['madrasha_slug']
        queryset = super().get_queryset().filter(madrasha__slug=madrasha_slug)
        return queryset

    def get_serializer_class(self):
        return HallDutySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class HallNigranDetailView(APIView):

    def get_object(self, pk):
        try:
            return HallDuty.objects.get(id=pk)
        except HallDuty.DoesNotExist:
            return Http404

    def get(self, request, pk, formate=None):
        obj = self.get_object(pk)
        serializer = HallDutySerializer(obj)
        return Response({"status": True, "data": serializer.data})

    def put(self, request, pk, formate=None):
        obj = self.get_object(pk)
        serializer = HallDutySerializer(obj, data=request.data)
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

    def delete(self, request, pk, format=None):
        exam_announcement = self.get_object(pk)
        exam_announcement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
