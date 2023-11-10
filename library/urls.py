from django.urls import path
from library.views import AuthorView, BookCategoryView, BookView

urlpatterns = [
    path('author/', AuthorView.as_view(), name='authors'),
    path('category/', BookCategoryView.as_view(), name='bookcategories'),
    path('book/', BookView.as_view(), name='book')
]