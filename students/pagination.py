from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
<<<<<<< HEAD
    page_size = 10
=======
    page_size = 3
>>>>>>> d6bb27bf7b982d4893faaee6150f762e3ec2bd27
    page_size_query_param = 'records'
    max_page_size = 10
