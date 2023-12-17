from django.shortcuts import render
from courses.serializers import CourseListSerializer
from rest_framework import generics
from courses.models import Course


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer

    
     
