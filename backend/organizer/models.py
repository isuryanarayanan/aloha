from django.db import models
from accounts.models import User
from django.db.models import TextField


class NonStrippingTextField(TextField):
    """A TextField that does not strip whitespace at the beginning/end of
    it's value.  Might be important for markup/code."""

    def formfield(self, **kwargs):
        kwargs['strip'] = False
        return super(NonStrippingTextField, self).formfield(**kwargs)

# Create your models here.

class Event(models.Model):
    """ Events that are conducted """

    name = models.CharField(max_length=250)
    short_description = models.TextField(default='')
    description =models.TextField(default='')
    timing = models.CharField(max_length=250)
    venue= models.CharField(max_length=250,default="")
    organizers = models.CharField(max_length=1550,default="")
    attendees = models.ManyToManyField(User,blank=True)
    team_based = models.BooleanField(default=False)
    teams = models.TextField(default="", blank=True)
    poster = models.TextField(blank=True)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

