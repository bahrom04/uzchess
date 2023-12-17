from django.urls import path
from courses.views import CourseListView


urlpatterns = [
    path('list/', CourseListView.as_view(), name='course-list'),

]