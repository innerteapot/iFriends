from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class RequestEvent(models.Model):
    event = models.CharField('Event', max_length=30)
    date = models.DateTimeField('Date')
    user = models.ForeignKey(User)
    addr = models.CharField('IP Address', max_length=20)
    url = models.CharField('Url', max_length=80)

    def __str__(self):
        return '%s - %s' % (self.event, self.date)

    class Admin:
        pass

class ViewEvent(models.Model):
    event = models.CharField('Event', max_length=30)
    date = models.DateTimeField('Date')
    user = models.ForeignKey(User)
    addr = models.CharField('IP Address', max_length=20)
    view = models.CharField('View', max_length=80)
    args = models.TextField('Args', max_length=200)
    kwargs = models.TextField('KWArgs', max_length=400)

    def __str__(self):
        return '%s - %s' % (self.event, self.date)

    class Admin:
        pass

class ResponseEvent(models.Model):
    event = models.CharField('Event', max_length=30)
    date = models.DateTimeField('Date')
    user = models.ForeignKey(User, blank=True, null=True)
    addr = models.CharField('IP Address', max_length=20)
    url = models.CharField('Url', max_length=80)
    size = models.IntegerField('Size')

    def __str__(self):
        return '%s - %s' % (self.event, self.date)

    class Admin:
        pass

class ExceptionEvent(models.Model):
    event = models.CharField('Event', max_length=30)
    date = models.DateTimeField('Date')
    user = models.ForeignKey(User)
    addr = models.CharField('IP Address', max_length=20)
    url = models.CharField('Url', max_length=80)
    exception = models.CharField('Exception', max_length=100)

    def __str__(self):
        return '%s - %s' % (self.event, self.date)

    class Admin:
        pass
