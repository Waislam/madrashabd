from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'records'
    max_page_size = 5
