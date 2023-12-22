from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    name = models.CharField("Photo name", max_length=250, null=True)
    slug = models.SlugField("Slug fiels", max_length=250, null=True)
    image = models.ImageField(upload_to='post_images/', null=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'

        indexes = [
            models.Index(fields=['-created']),
            ]


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Photo, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
        indexes = [models.Index(fields=["created_at"])]

    def __str__(self):
        return f"{self.user.username} - {self.post.name} - {self.created_at}"