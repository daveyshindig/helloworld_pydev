from django.db import models
import datetime
from django.utils import timezone


# This module contains Django models that constitute a simple polling system.

class MyPoll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    # Unicode is used throughout Django's automatically-generated admin,
    # also good for my sanity when dealing with Django's interactive shell.
    def __unicode__(self): 
        return self.question
    
    # Note the above are normal Python methods. Let's add a custom method, 
    # just for demonstration:
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class MyChoice(models.Model):
    poll = models.ForeignKey(MyPoll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    
    # Unicode is used throughout Django's automatically-generated admin, etc.
    def __unicode__(self):
        return self.choice