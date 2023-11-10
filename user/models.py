from django.db import models
from courses.models import Course
from library.models import Book


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    birthday = models.DateField()
    image = models.ImageField(upload_to='static/user_images/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    courses = models.ManyToManyField(Course)
    # orders

    def __str__(self):
        return self.username
    

class FavouriteBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - liked books"


class FavouriteCource(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - liked cources"