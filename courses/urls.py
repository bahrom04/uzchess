from django.urls import path
from courses import views

# app_name = "course"

urlpatterns = [
    path("list/", views.CourseApiView.as_view(), name="course-list"),
    path("<int:course_id>/", views.CourseDetailApiView.as_view(), name="detail-course"),
    # path("delete/<int:id>/", views.CourseDeleteApiView.as_view(), name="delete-course"),
]
