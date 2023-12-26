from django.urls import path
from courses import views

app_name = "courses"

urlpatterns = [
    # Course
    path("list/", views.CourseApiView.as_view(), name="course-list"),
    path("<int:course_id>/", views.CourseDetailApiView.as_view(), name="course-detail"),
]
