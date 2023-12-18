from django.db import models

class Pers(models.Model):
    title = models.CharField('name', max_length=50)
    story = models.TextField('story')
    age = models.CharField('age', max_length=40)
    image = models.ImageField(upload_to='post_images/', null=True,)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'character'
        verbose_name_plural = 'characters'
