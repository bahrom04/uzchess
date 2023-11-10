from django.db import models


LEVEL_CHOICES = (
    ('Beginner', 'Beginner'),
    ('Amateur', 'Amateur'),
    ('Professional', 'Professional'),    
)
RATING_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class Author(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    

class BookCategory(models.Model):

    '''Category for each book'''

    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/library_images/')
    description = models.TextField()
    price = models.IntegerField()
    published_date = models.DateTimeField()
    total_pages = models.IntegerField()

    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    is_favourite = models.BooleanField(default=False)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['-created_at']

    def __str__(self):
        return self.title