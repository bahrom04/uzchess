from rest_framework import serializers
from users.models import User
from courses.models import (
    Course,
    Category,
    CourseComment,
    CourseChapter,
    CourseLesson,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class CourseCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CourseComment
        fields = ("user", "rating", "title", "created_at")


class CourseLessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLesson
        fields = ("title", "description", "video_path")


class CourseChapterListSerializer(serializers.ModelSerializer):
    lesson = CourseLessonListSerializer(many=True)

    class Meta:
        model = CourseChapter
        fields = ("title", "description", "lesson")


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("title", "image", "lavel", "discount", "category")


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    chapter = CourseChapterListSerializer(read_only=True, many=True)
    comment = CourseCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ("id", "title", "image", "lavel", "discount", "category", "chapter", "comment")
