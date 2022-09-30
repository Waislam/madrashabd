from .models import LibraryBook
import django_filters


class BookFilter(django_filters.FilterSet):
    # user__phone = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = LibraryBook
        fields = ['name']
