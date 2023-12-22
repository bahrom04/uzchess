from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from courses.models import Course
from courses.permissions import CustomAccessPermission
from courses.serializers import (
    CourseListSerializer,
    CourseCreateUpdateDeleteSerializer,
)


class CourseApiView(APIView):
    def get(self, request, format=None):
        """
        List courses
        """
        course = Course.objects.all()
        serializer = CourseListSerializer(course, many=True)
        if type(course) == Response:
            return course
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create course
        """
        serializer = CourseCreateUpdateDeleteSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(CourseListSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# course/{course_id}
class CourseDetailApiView(APIView):
    permission_classes = [CustomAccessPermission]

    def get(self, request, course_id):
        """
        View individual course
        """
        course = get_object_or_404(Course, pk=course_id)
        serializer = CourseListSerializer(course)
        return Response(serializer.data)

    def patch(self, request, course_id):
        """
        Update post
        """
        course = get_object_or_404(Course, pk=course_id)
        serializer = CourseCreateUpdateDeleteSerializer(
            course, data=request.data, context={"request": request}, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(CourseCreateUpdateDeleteSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, course_id):
        """
        Delete post
        """
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return Http404("Course not found")
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
