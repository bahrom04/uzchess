from django.contrib import admin
from courses.models import Course, Chapter, Lesson, UserLessonRewiew, CourseComment


admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Lesson)
admin.site.register(UserLessonRewiew)
admin.site.register(CourseComment)