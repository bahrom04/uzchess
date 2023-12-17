from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from courses.models import Course
from django.contrib.auth import get_user_model


class CousesTests(APITestCase):
    def setUp(self):

        User = get_user_model()

        course_data = {
            "title": "Shaxmat bilan tanishuv",
            "image": None,
            "level": "Beginner",
            "price": "50",
            "discount": "100",
            "is_saved": False,
        }

        user = User.objects.create_user(username='user1', password='parol123')
        admin = User.objects.create_superuser(username='admin', password='parol123')

        
        def create_cource():
            return Course.objects.create(**course_data)
        
        
        self.user = user
        self.admin = admin
        self.course = course_data
        self.create_cource = create_cource

    
    def test_get_null_course(self):
        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)




