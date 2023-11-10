from django.db import models


DIFFICULTY_LEVEL = (
    ('Beginner', 'Beginner'),
    ('Amateur', 'Amateur'),
    ('Professional', 'Professional'),
)


class MainSubClass(models.Model):
    # get class number by id:
    # example day 1. Asosiy donalar -> id=1 
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class SubClass(models.Model):
    # example: 1.1
    class_number = models.FloatField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to='static/course-class_videos/')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    belongs_to = models.ForeignKey(MainSubClass, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    

class Course(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/courses_images/')
    price = models.IntegerField()
    total_chapters = models.IntegerField()
    total_classes = models.IntegerField()
    rating = models.FloatField(default=0.0)
    lavel = models.CharField(max_length=20, choices=DIFFICULTY_LEVEL)

    main_sub_class = models.ForeignKey(MainSubClass, on_delete=models.CASCADE)

    discount = models.IntegerField(default=0)
    is_purchased = models.BooleanField(default=False)
    is_saved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    # owner from user
    title = models.TextField()
    rating = models.FloatField()
    is_complained = models.BooleanField(default=False)
    created_at = models.DateTimeField()

    belongs_to = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.title