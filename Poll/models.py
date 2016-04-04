from django.db import models
from People.models import Person

# Create your models here.

class UserPoll(models.Model):
    question = models.CharField('Question', max_length=100)
    date = models.DateTimeField('Creation Date')
    person = models.ForeignKey(Person)

    def __str__(self):
        return '%s' % (self.question)


class Opinion(models.Model):
    poll = models.ForeignKey(UserPoll)
    opinion = models.CharField('Opinion', max_length=50)
    votes = models.IntegerField('Vote Count')

    def __str__(self):
        return '%s' % (self.opinion)
