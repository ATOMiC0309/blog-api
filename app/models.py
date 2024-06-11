from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text="Qaysi kategoriyaga tegisgli post!")
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='post-images/', blank=True, null=True, help_text="Agar postda rasm bo'lsa!")
    like_count = models.IntegerField(default=0)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Author: {self.author}. Comment: {self.text[:200]}"
