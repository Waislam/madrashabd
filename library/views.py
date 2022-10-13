from django.http import Http404
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.generics import mixins, GenericAPIView
from rest_framework.views import APIView

from library.filters import BookFilter
from library.models import LibraryBook
from library.serializers import LibraryBookCreateSerializer, LibraryBookUpdateSerializer
from students.pagination import CustomPagination


# Create your views here.


class LibaryBookView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     GenericAPIView):

    queryset = LibraryBook.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    serializer_class = LibraryBookCreateSerializer
    filterset_class = BookFilter
    search_fields = ['number']
    pagination_class = CustomPagination

    def get_queryset(self):
        """getting any argument/parameter from api/url"""
        madrasha_slug = self.kwargs['madrasha_slug']
        return super(LibaryBookView, self).get_queryset().filter(madrasha__slug=madrasha_slug)

    def get(self, request, *args, **kwargs):
        """method to show the list of Teacher """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Method to create Teacher obj """
        # print('kwargs', **kwargs)
        return self.create(request, *args, **kwargs)


class BookDetailView(APIView):
    """ put, get, no delete"""
    def get_object(self, pk):
        """get single obj"""
        try:
            return LibraryBook.objects.get(id=pk)
        except LibraryBook.DoesNotExist:
            raise Http404

    def get(self, request, pk, formate=None):
        """veiw details of single obj"""
        book = self.get_object(pk)
        serializer = LibraryBookCreateSerializer(book)
        return Response({'status': True, 'data': serializer.data})

    def put(self, request, pk, formate=None):
        """update single teacher"""
        book = self.get_object(pk)
        serializer = LibraryBookUpdateSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'data': serializer.data})
        return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

