from django.db import models

class Artiles(models.Model):
    title = models.CharField('news name', max_length=50)
    full_text = models.TextField('article')
    date = models.DateTimeField('date time')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'