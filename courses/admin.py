from django.contrib import admin
from .models import MainSubClass, SubClass, Comment, Course

# task:change new models name
admin.site.register(MainSubClass)
admin.site.register(SubClass)
admin.site.register(Comment)
admin.site.register(Course)

