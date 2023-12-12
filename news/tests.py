from django.test import TestCase
from news.models import News


class NewsTestCace(TestCase):
    def setUp(self):
        News.objects.create(title='first',content='first')
        News.objects.create(title='second',content='second')

    
    


