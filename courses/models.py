from django.db import models
from user.models import User

'''
task: import BaseModel From common/models.py instead of models.Model
'''

DIFFICULTY_LEVEL = (
    ('Beginner', 'Beginner'),
    ('Amateur', 'Amateur'),
    ('Professional', 'Professional'),
)


class Chapter(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'Chapter'
        verbose_name_plural = 'Chapters'

    def __str__(self):
        return self.title


# Video Lessons
class Lesson(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField()
    video_path = models.FileField(upload_to='static/course-class_videos/')

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.title
    

class Course(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/courses_images/')
    price = models.IntegerField()
    # total_chapters = models.IntegerField()
    # total_classes = models.IntegerField()
    # rating = models.FloatField(default=0.0)
    lavel = models.CharField(max_length=20, choices=DIFFICULTY_LEVEL)

    discount = models.IntegerField(default=0)
    is_purchased = models.BooleanField(default=False)
    is_saved = models.BooleanField(default=False)
    # is_free = models.BooleanField(default=False) not used yet


    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title
    

# User progress
class UserLessonRewiew(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vieo_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    last_watched = models.DateTimeField(blank=True, null=True)
    is_finished = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'UserRewiew'
        verbose_name_plural = 'UserRewiews'

    def __str__(self):
        return f"{self.user.username} - {self.vieo_lesson.title}"


class CourceComment(models.Model):
    # task: create custom user
    # author = models.ForeignKey(
    #     CustomUser, on_delete=models.CASCADE, related_name="coursecomment_author", verbose_name=_("Author")
    #                            )
    rating = models.PositiveSmallIntegerField()
    title = models.TextField()
    is_complained = models.BooleanField(default=False)

    cource = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'CourceComment'
        verbose_name_plural = 'CourceComments'
        
    def __str__(self):
        return f"{self.cource.title} - rating:{self.title}"