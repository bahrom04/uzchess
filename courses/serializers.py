from courses.models import Course, Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title",)


class CourseListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = ("title", "image", "lavel", "discount", "category")


class CourseCreateUpdateDeleteSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = ("title", "image", "lavel", "discount", "category")
