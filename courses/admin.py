from django.contrib import admin
from .models import Chapter, Lesson, Course, UserLessonRewiew, CourceComment

# task:change new models name
admin.site.register(Chapter)
admin.site.register(Lesson)
admin.site.register(Course)
admin.site.register(UserLessonRewiew)
admin.site.register(CourceComment)

