from .models import Committee
import django_filters


class CommitteeFilter(django_filters.FilterSet):
    class Meta:
        model = Committee
        fields = ['phone_number', 'member_name']


