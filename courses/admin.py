from django.contrib import admin
from courses.models import Course, CourseChapter, CourseLesson, UserLessonRewiew, CourseComment


admin.site.register(Course)
admin.site.register(CourseChapter)
admin.site.register(CourseLesson)
admin.site.register(UserLessonRewiew)
admin.site.register(CourseComment)