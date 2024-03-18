from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookViewSet.as_view({'get': 'list'}), name='book-list'),
    # Add more URL patterns for other views as needed
]
