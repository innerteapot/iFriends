from django.db import models
from django.contrib.auth.models import User

# Create your models here.

gender_list = (('M', 'Male'), ('F', 'Female' ))

class Blog(models.Model):
    title = models.CharField('Title', max_length=200)
    text = models.TextField('Text', max_length=2048)
    date = models.DateTimeField('Last Modified')

    def __str__(self):
        return '%s' % (self.title)

    def blog_size (self):
        return len(self.text)

    class Meta:
        permissions = (
            ('can_blog', 'Allowed to Blog'),
        )


class Person(models.Model):
    userID = models.ForeignKey(User, unique=True)
    name = models.CharField('name', max_length=200)
    birthday = models.DateField('Birthday', blank=True, null=True)
    gender = models.CharField(max_length=1, choices=gender_list)
    email = models.EmailField('Email', max_length=100, unique=True)
    favoriteURL = models.URLField('myURL')
    desc = models.TextField('Desc', max_length=500, null=True)
    friends = models.ManyToManyField('self', blank=True)
    blogs = models.ManyToManyField(Blog, blank=True)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        permissions = (
            ('can_add_friends', 'Can Add Friends'),
        )

