from django.db import models
from courses.models import Course
from library.models import Book
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Favourite(models.Model):
    user   = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    book   = models.ManyToManyField(
        Book, blank=True, related_name='favourite'
        )
    course = models.ManyToManyField(
        Course, blank=True, related_name='favourite'
        )

    
    def __str__(self):
        return f"{self.user.username} - favourite "

