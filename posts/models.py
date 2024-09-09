from django.db import models
from django.contrib.auth.models import User
from category.models import Category

class Post(models.Model):
    """
    Post model, related to User
    """
    image_filter_choices = [
        ('fun', 'Fun'),
        ('food', 'Food'),
        ('nature', 'Nature'),
        ('health', 'Health'),
        ('pet', 'Pet'),
        ('cat', 'Cat'),
        ('dog', 'Dog'),
        ('bird', 'Bird'),
        ('2024', '2024'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_htbmpw', blank=True
    )
    image_filter = models.CharField(
        max_length=32,
        choices=image_filter_choices,
        default='Pet'
    )
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

