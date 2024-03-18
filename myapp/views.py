from rest_framework import viewsets
from myapp.models import Book
from myapp.serializers import BookSerializer
from rest_framework import pagination

class BookPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000

class BookViewSet(viewsets.ModelViewSet):
    """ This is an API endpoint that allows books to be viewed. """

    lookup_field = 'gutenberg_id'

    queryset = Book.objects.exclude(download_count__isnull=True)
    queryset = queryset.exclude(title__isnull=True)

    serializer_class = BookSerializer
    pagination_class = BookPagination

    def get_queryset(self):
        queryset = self.queryset

        # Your existing queryset filtering logic here

        return queryset.distinct()
