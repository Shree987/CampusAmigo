from django.db import models
import datetime


# Create your models here.
class Club(models.Model):
    """Model representing a club."""
    name = models.CharField(max_length=100,help_text='Name of the club',verbose_name='Name')                
    convener = models.CharField(max_length=100,help_text='Name of the convener',verbose_name='Convener')
    email = models.EmailField(max_length=1000,help_text='Club email id',verbose_name='Email Id')
    mobile_no = models.IntegerField(verbose_name='Mobile Number')
    logo = models.ImageField(upload_to=None,width_field=None,height_field=None)
    username = models.CharField(max_length=100,verbose_name='Username')
    password = models.CharField(max_length=100,verbose_name='Password')
    website = models.URLField(verbose_name='Website link')
    technical = models.BooleanField(default=False)
    exclusive = models.BooleanField(default=False)

    def __str__(self):
        """String to represent the model."""
        return self.name

class Student(models.Model):
    """Model representing a member."""
    name = models.CharField(max_length=100,help_text='Name of the member',verbose_name='Name')
    username = models.CharField(max_length=100,verbose_name='Username')
    password = models.CharField(max_length=100,verbose_name='Password')
    branch = models.CharField(max_length=100,verbose_name='Branch')
    mobile_no = models.IntegerField(verbose_name='Mobile Number')
    email = models.EmailField(max_length=1000,help_text='Club email id',verbose_name='Email Id')
    roll_no = models.CharField(max_length=8,help_text='Branchwise Roll Number',verbose_name='Roll Number')

    def __str__(self):
        """String to represent the model."""
        return self.name

class Event(models.Model):
    """Model representing an event by a club."""

    club = models.ForeignKey('Club',on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100,verbose_name='Event Name')
    description = models.CharField(max_length=500,verbose_name='Description',help_text='short description of the event')
    date = models.DateField(verbose_name='Date')
    time = models.TimeField(verbose_name='Time')
    venue = models.CharField(default='NULL',max_length=100,verbose_name='Venue')

    def __str__(self):
        """String to represent the model."""
        return self.event_name    
