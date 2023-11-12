from django.contrib import admin
from .models import News, Socials
from ckeditor_uploader.widgets import CKEditorUploadingWidget



# Register your models here.
admin.site.register(News)
admin.site.register(Socials)
