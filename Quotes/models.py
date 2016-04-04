from django.db import models

# Create your models here.

class Quote(models.Model):
    text = models.TextField('text', max_length=200)
    by = models.CharField ('by', max_length=50)

    def __str__(self):
        return '%s' % (self.text)
    class Admin:
       pass
