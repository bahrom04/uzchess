from rest_framework import serializers
from . models import Author, BookCategory, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = BookCategorySerializer()

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'image',
            'description',
            'price',
            'published_date',
            'total_pages',
            'category',
            'is_favourite',
            'author',
            'level',
            'rating',
            'author',
            'category',
        ]