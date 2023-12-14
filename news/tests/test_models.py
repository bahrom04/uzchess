from news.models import Socials, News
from django.test import TestCase

class SocialsTest(TestCase):
    def setUp(self):
        Socials.objects.create(title='Telegram')
        Socials.objects.create(title='Twitter')

    def test_socials_title(self):
        socials_telegram = Socials.objects.get(title='Telegram')
        socials_twitter = Socials.objects.get(title='Twitter')

        self.assertEqual(socials_telegram.title, 'Telegram')
        self.assertEqual(socials_twitter.title, 'Twitter')


