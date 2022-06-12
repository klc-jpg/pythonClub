from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Event, Resource
from django.urls import reverse
from .views import index, resources_view, meetings_view,  meeting_detail
from datetime import datetime

# Create your tests here.
class MeetingTest(TestCase):
    def setUpMeet(self):
        self.meetDetail=Meeting(meetingtitle='TBD')#, meetingdate='July 6, 2022', meetingtime='5:00 pm', meetinglocation='TBD', meetingagenda='• TBD • TBD • TBD')
        return self.meetDetail

    def test_string_meet(self):
        meetDetail=self.setUpMeet()  
        self.assertEqual(str(self.meetDetail), meetDetail.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')


class MeetingMinutes(TestCase):
    def setUpMin(self):
        self.meetDetail=Meeting(meetingtitle='TBD')
        self.meetMins= MeetingMinutes(meetingid=self.meetDetail)
        return self.meetMins
        
    def test_string_min(self):
        self.meetMins=MeetingMinutes.setUpMin(self)
        self.meetDetail=Meeting(meetingtitle='TBD')
        self.assertEqual(str(self.meetMins), MeetingMinutes )

    def test_table_min(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')


class ResourceTest(TestCase):
    def setUpRec(self):
        self.resource=Resource(resourcename='Trinket.io')
        return self.resource

    def test_string_resource(self):
        resource=self.setUpRec()  
        self.assertEqual(str(self.resource), resource.resourcename)

    def test_table_resource(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')


class meetingDetailTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='kelly')
        self.meetMins1=MeetingMinutes.objects.create(meetingid=self.meetDetail, attendance=self.u, minutestext='')
        self.meetMins1=User.add(self.u)
        self.meetDetail=Meeting.objects.create(meetingtitle='TBD', meetingdate='July 6, 2022', meetingtime='5:00 pm', meetinglocation='TBD', meetingagenda='• TBD • TBD • TBD')
       