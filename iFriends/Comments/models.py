from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField('title', max_length=200)
    text  = models.CharField('text', max_length=500)

    def __str__(self):
        return '%s' % (self.title)

    class Admin:
        pass

