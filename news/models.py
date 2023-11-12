from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Social media links
class Socials(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/socials/')
    
    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'

    def __str__(self):
        return self.title
    

class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/news_images/')
    content = RichTextUploadingField()
    views = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title