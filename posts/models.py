from django.db import models
from django.contrib.auth.models import User

CATEGORIES = (
    ("pet", "Pet"),
    ("dog", "Dog"),
    ("cat", "Cat"),
    ("bird", "Bird"),
    ("bunny", "Bunny"),
    ("food", "Food"),
    ("accessories", "Accessories"),
)

class Post(models.Model):
    """
    Post model, related to User
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_htbmpw', blank=True
    )
    category = models.CharField(
        max_length=50, choices=CATEGORIES, default='Pet'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

