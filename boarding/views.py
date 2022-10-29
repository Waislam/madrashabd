from rest_framework import status, generics
from rest_framework.generics import mixins, GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import BazarList
from .serializers import BazarListSerializer
from .filters import BazarListFilter
from .pagination import CustomPagination


class BazarListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView
):
    queryset = BazarList.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    serializer_class = BazarListSerializer
    filterset_class = BazarListFilter
    search_fields = ['date']
    pagination_class = CustomPagination

    def get_queryset(self):
        """getting any argument/parameter from api/url"""
        madrasha_slug = self.kwargs['madrasha_slug']
        return super(BazarListView, self).get_queryset().filter(madrasha__slug=madrasha_slug)
        # return super(BazarListView, self).get_queryset()

    def get(self, request, *args, **kwargs):
        """method to show the list of Teacher """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Method to create Teacher obj """
        # print('kwargs', **kwargs)
        return self.create(request, *args, **kwargs)
