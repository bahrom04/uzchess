from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField
from common.models import BaseModel


# Social media links
class Socials(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/socials/')
    
    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'

    def __str__(self):
        return self.title
    

class News(BaseModel):
    title   = models.CharField(max_length=255)

    image   = models.ImageField(upload_to='uzchess_clone/static/news_images/', null=True, blank=True)
    _image  = models.ImageField(upload_to='uzchess_clone/static/news_images/', null=True, blank=True, editable=False)

    content =  models.TextField()
    views   = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
    
    @property
    def image(self):
        return self.image if self.image else None
    
    def __str__(self):
        return self.title
    
    def add_views(self):
        self.views +=1
        self.save()
        