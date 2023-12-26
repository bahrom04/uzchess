from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from courses.models import Course, Category


class BaseApiTestCase(APITestCase):
    def setUp(self):
        super().setUp()

        User = get_user_model()
        user1_data = {"username": "test_username1", "password": "password123"}
        admin_data = {"username": "admin", "password": "admin"}

        category_title = {
            "title": "shaxmat"
        }
        course_data = {
            "title": "Shaxmat bilan tanishuv",
            "image": None,
            "lavel": "Beginner",
            "price": "50",
            "discount": "100",
            "is_saved": False,
            "category": category_title
        }
        self.user1 = User.objects.create(**user1_data)
        self.category = Category.objects.create(**category_title)
        self.course = Course.objects.create(**course_data)
        self.course.save()
