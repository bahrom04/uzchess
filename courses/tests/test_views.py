from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from courses import models
from users.models import User
from .base import BaseApiTestCase


class CourseApiViewTestCase(BaseApiTestCase):
    def test_course_list(self):
        response = self.client.get(reverse("courses:list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Beginner")
