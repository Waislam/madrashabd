from rest_framework import status, generics
from rest_framework.generics import mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import BazarList
from .serializers import BazarListSerializer
from .filters import BazarListFilter
from accounts.models import Madrasha
from .pagination import CustomPagination


class BazarListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    """BazarList Create and list view"""

    # queryset = BazarList.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BazarListFilter
    search_fields = ["date"]
    pagination_class = CustomPagination
    serializer_class = BazarListSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return BazarList.objects.filter(madrasha__slug=slug)

    def get(self, request,  *args, **kwargs):
        """method to show the list of Students"""

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Method to create student obj"""
        return self.create(request, *args, **kwargs)