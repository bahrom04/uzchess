from django.contrib import admin
from .models import Author, BookCategory, Book


admin.site.register(Author)
admin.site.register(BookCategory)
admin.site.register(Book)

