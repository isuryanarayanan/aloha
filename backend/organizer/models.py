from django.db import models
from accounts.models import User

# Create your models here.

class Event(models.Model):
    """ Events that are conducted """

    name = models.CharField(max_length=250)
    short_description = models.TextField(default='')
    description = models.TextField(default='')
    timing = models.CharField(max_length=250)
    venue= models.CharField(max_length=250,default="")
    organizers = models.CharField(max_length=1550,default="")
    attendees = models.ManyToManyField(User,blank=True)
    team_based = models.BooleanField(default=False)
    teams = models.TextField(default="", blank=True)

    def __str__(self):
        return self.name


