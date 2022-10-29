from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Committee
from .serializers import CommitteeSerializers, CommitteeListSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import CommitteeFilter
from .pagination import CustomPagination
from rest_framework.generics import mixins, GenericAPIView


class CommitteeListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView
):
    queryset = Committee.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    serializer_class = CommitteeSerializers
    filterset_class = CommitteeFilter
    search_fields = ['member_name', 'phone_number']
    pagination_class = CustomPagination

    def get_queryset(self):
        """getting any argument/parameter from api/url"""
        # madrasha_slug = self.kwargs['madrasha_slug']
        return super(CommitteeListView, self).get_queryset()
        # return super(CommitteeListView, self).get_queryset().filter(madrasha__slug=madrasha_slug)

    def get(self, request, *args, **kwargs):
        """method to show the list of Committee """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Method to create Committee obj """
        # print('kwargs', **kwargs)
        return self.create(request, *args, **kwargs)


class CommitteeDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Committee.objects.get(pk=pk)
        except Committee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = CommitteeListSerializers(queryset)
        return Response(serializer.data)

    def put(self, request, pk, formate=None):
        """update single obj details"""
        queryset = self.get_object(pk)
        serializer = CommitteeSerializers(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": True,
                 "message": "Student Income has been updated successfully",
                 "data": serializer.data,
                 }
            )
        return Response(
            {"status": False, "message": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
