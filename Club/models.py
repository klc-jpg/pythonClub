from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.CharField(max_length=255)
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.TextField(null=True, blank=True, help_text='Add meeting agenda details')

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table="meeting"
        verbose_name_plural="meetings"

class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)            
    #user=models.ManyToManyField(User, verbose_name='attendance')
    #attendance=models.TextField(max_length=255)
    minutestext=models.TextField(null=True, blank=True)
    #user=models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='attendance', null=True, blank=False)
    attendance=models.ManyToManyField(User)

    def __str__(self):
        return self.meetingid

    class Meta:
        db_table="meetingminutes"
        verbose_name_plural='meeting minutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField(null=True, blank=True)
    #user=models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='resourceentrydate')
    resourceentrydate=models.ForeignKey(User, auto_now_add=False)
    resourcedescription=models.TextField(null=True, blank=True, help_text='Add details about this resource')

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table="resource"
        verbose_name_plural="resources"

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.CharField(max_length=255)
    eventdescription=models.TextField(null=True, blank=True, help_text='Add details about the event')
    #user=models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='memberid', null=True, blank=False)
    memberid=models.CharField(max_length=255, null=True, blank=False)

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table="event"
        verbose_name_plural="events"

    



