from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='post_images/', null=True, )



    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'



