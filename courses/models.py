from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from common.models import BaseModel


class Course(BaseModel):

    DIFFICULTY_LEVEL = (
        ('Beginner', 'Beginner'),
        ('Amateur', 'Amateur'),
        ('Professional', 'Professional'),
    )

    title        = models.CharField(max_length=255)
    image        = models.ImageField(upload_to='uzchess_clone/static/courses_images/', blank=True)
    lavel        = models.CharField(max_length=32, choices=DIFFICULTY_LEVEL)

    price        = models.PositiveIntegerField(default=0)
    discount     = models.PositiveIntegerField()

    is_saved     = models.BooleanField(default=False)
    slug         = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title
    
    def is_discount(self):
        return False if self.price==0 else True
    
    def is_user_purchased(self, user):
        return self.user_lesson.filter(user=user, is_active=True).exists()
    
    def user_purchase(self, user):
        if not self.is_user_purchased(user):
            UserLessonRewiew.objects.create(user=user, cource=self)
            return True
        return False
    
    def user_cancel(self, user):
        if self.is_user_purchased(user):
            UserLessonRewiew.objects.get(user=user).delete()
            
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        super(Course, self).save(*args, **kwargs)


class Chapter(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Chapter'
        verbose_name_plural = 'Chapters'

    def __str__(self):
        return self.title


# Video Lessons
class Lesson(BaseModel):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField()
    video_path = models.FileField(upload_to='static/course-class_videos/')

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.title
    
   
# User progress
class UserLessonRewiew(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='user_lesson')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'UserRewiew'
        verbose_name_plural = 'UserRewiews'

    @property
    def user_lesson(self):
        return f"{self.user.username} - {self.course.title}"


class CourseComment(models.Model):
    rating        = models.DecimalField(decimal_places=1)
    title         = models.TextField()
    
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    cource        = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'CourceComment'
        verbose_name_plural = 'CourceComments'
        
    @property
    def user_comment_info(self):
        return f"{self.user} comment on {self.cource}"