from django.test import TestCase

# Create your tests here.
class TestNewsList(TestCase):

    def test_news(self):

        response = self.client.get('/api/news/')
        self.assertEqual(response.status_code, 200)


class TestSocials(TestCase):

    def test_socials(self):

        response = self.client.get('/api/socials/')
        self.assertEqual(response.status_code, 200)
