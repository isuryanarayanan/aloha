from django.db import models
from accounts.models import User

# Create your models here.

class Event(models.Model):
    """ Events that are conducted """

    name = models.CharField(max_length=250)
    description = models.TextField(default='')
    timing = models.CharField(max_length=250)
    organizers = models.CharField(max_length=550,default="")
    attendees = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.name


