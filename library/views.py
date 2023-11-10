from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'


class AuthorView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookCategoryView(generics.ListAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


class BookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class TopBooksView(generics.ListAPIView):
    queryset = Book.objects.all().filter(is_Top=True)
    serializer_class = BookSerializer
    # use api/topbooks/?size='YOUR_SIZE' 
    pagination_class = CustomPageNumberPagination
