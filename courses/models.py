from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from common.models import BaseModel

User = get_user_model()


class Category(BaseModel):
    title = models.CharField(max_length=255)


class Course(BaseModel):
    class Difficulty_lavel(models.TextChoices):
        Beginner = "Beginner", "Beginner"
        Amateur = "Amateur", "Beginner"

    class Language(models.TextChoices):
        Uzbek = "Uz", "uz"
        English = "Eng", "eng"
        Russian = "Ru", "ru"

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uzchess_clone/static/courses_images/", blank=True)
    lavel = models.CharField(max_length=32, choices=Difficulty_lavel.choices)
    price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField()

    is_saved = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="course")

    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title

    def is_course_saved(self):
        return self.user_lesson.is_saved if True else False

    def is_discount(self):
        return False if self.price == 0 else True

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


class CourseChapter(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="chapter")

    class Meta:
        verbose_name = "Chapter"
        verbose_name_plural = "Chapters"

    def __str__(self):
        return self.title


# Video Lessons
class CourseLesson(BaseModel):
    chapter = models.ForeignKey(CourseChapter, on_delete=models.CASCADE, related_name="lesson")

    title = models.CharField(max_length=255)
    description = models.TextField()
    video_path = models.FileField(upload_to="static/course-class_videos/")

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

    def __str__(self):
        return self.title


# User progress
class UserLessonRewiew(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="user_lesson")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "UserRewiew"
        verbose_name_plural = "UserRewiews"

    @property
    def user_lesson(self):
        return f"{self.user.get_username()} - {self.course.title}"


class CourseComment(models.Model):
    rating = models.DecimalField(decimal_places=1, max_digits=2)
    title = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cource = models.ManyToManyField(Course, blank=False, related_name="comment")

    class Meta:
        verbose_name = "CourceComment"
        verbose_name_plural = "CourceComments"

    @property
    def user_comment_info(self):
        return f"{self.user.get_username()} comment on {self.cource}"
