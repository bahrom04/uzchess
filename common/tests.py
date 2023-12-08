from django.test import TestCase

# Create your tests here.

class TestUserFavourite(TestCase):

    def test_index(self):

        response = self.client.get('user_name/favourite/')
        self.assertEqual(response.status_code, 200)


    def test_404(self):
        response = self.client.get('user_name/favourite/')
        self.assertEqual(response.status_code, 404)



