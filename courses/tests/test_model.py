from .base import BaseApiTestCase


class CourseModelApiTestCase(BaseApiTestCase):
    def test_course_data(self):
        self.assertEqual(self.course.title, "Shaxmat bilan tanishuv")

    