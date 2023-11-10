from django.contrib import admin
from .models import MainSubClass, SubClass, Comment, Course


admin.site.register(MainSubClass)
admin.site.register(SubClass)
admin.site.register(Comment)
admin.site.register(Course)

