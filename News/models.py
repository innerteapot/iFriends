from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

class Announcement(models.Model):
    userID = models.ForeignKey(User)
    title = models.CharField('Title', max_length=200)
    text = models.TextField('Text', max_length=1024)
    date = models.DateTimeField('Published')
    sites = models.ManyToManyField(Site)
    objects = models.Manager()
    on_site = CurrentSiteManager('sites')

    def __str__(self):
        return '%s' % (self.title)

    class Admin:
        pass

class Story(models.Model):
    userID = models.ForeignKey(User)
    title = models.CharField('Title', max_length=200)
    text = models.TextField('Text', max_length=1024)
    date = models.DateTimeField('Published')
    site = models.ForeignKey(Site)
    objects = models.Manager()
    on_site = CurrentSiteManager()

    def __str__(self):
        return '%s' % (self.title)

    class Admin:
        pass
