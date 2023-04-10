from rest_framework.pagination import PageNumberPagination


class BasePageNumberPagination(PageNumberPagination):
    max_page_size = 100
    page_query_param = 'page'
    page_size = 10
    page_size_query_param = 'page-size'
