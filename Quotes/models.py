from django.db import models

# Create your models here.

class Quote(models.Model):
    text = models.TextField('text', max_length=200)
    by = models.CharField ('by', max_length=50)
    date = models.DateTimeField('Last Modified', auto_now=True)

    def __str__(self):
        return '%s' % (self.text)

    def get_absolute_url(self):
        return '/Quote/Detail/%d' % self.id

    class Admin:
       pass
