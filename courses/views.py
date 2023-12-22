from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from courses.models import Course
from courses.serializers import (
    CourseListSerializer,
    CourseCreateUpdateDeleteSerializer,
)


class CourseApiView(APIView):
    @staticmethod
    def get(request, format=None):
        """
        List courses
        """

        course = Course.objects.all()
        serializer = CourseListSerializer(course, many=True)
        if type(course) == Response:
            return course
        return Response(serializer.data)

    @staticmethod
    def post(request, format=None):
        """
        Create course
        """

        serializer = CourseCreateUpdateDeleteSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(CourseListSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailApiView(APIView):
    @staticmethod
    def get(request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        serializer = CourseListSerializer(course)
        return Response(serializer.data)
