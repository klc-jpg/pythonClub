from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Event, Resource
from django.urls import reverse, reverse_lazy
from .views import index, resources_view, meetings_view,  meeting_detail
from datetime import datetime
from .forms import ResourceForm, MeetingForm


# Create your tests here.
class MeetingTest(TestCase):
# Do I need to add these fields to setUpMeet: ,meetingdate='July 6, 2022', meetingtime='5:00 pm', meetinglocation='TBD', meetingagenda='• TBD • TBD • TBD')
    def setUpMeet(self):
        self.meetDetail=Meeting(meetingtitle='TBD')
        return self.meetDetail

    def test_string_meet(self):
        meetDetail=self.setUpMeet()  
        self.assertEqual(str(self.meetDetail), meetDetail.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')


class MeetingMinutesTest(TestCase):
    def setUpMin(self):
        self.meetDetail=Meeting(meetingtitle='TBD')
        self.meetMins= MeetingMinutes(meetingid=self.meetDetail)
        return self.meetMins
        
    def test_string_min(self):
        self.meetMins=MeetingMinutes.setUpMin(self)
        self.meetDetail=Meeting(meetingtitle='TBD')
        self.assertEqual(str(self.meetMins), MeetingMinutes )
        return str(self.meetingid)

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


class MeetingDetailTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='kelly')
        self.meetMins1=MeetingMinutes.objects.create(meetingid=self.meetDetail, attendance=self.u, minutestext='')
        self.meetMins1=User.add(self.u)
        self.meetDetail=Meeting.objects.create(meetingtitle='TBD', meetingdate='July 6, 2022', meetingtime='5:00 pm', meetinglocation='TBD', meetingagenda='• TBD • TBD • TBD')

#class ResourceFormTest(TestCase):
    #def test_resource_form(self):
     #   data= {
             #   {'resourcename':'Matplotlib', 
             #    'resourcetype':'Library', 
             #    'resourceurl':'https://matplotlib.org/', 
             #    'resourcedescription':'Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible',
           # }
       # }
       # form= ResourceForm(data)
       # self.assertTrue(form.is_valid)

class New_Resource_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testUserOne', password='AF&uWprZ7RHFVw')
        self.resource=Resource.objects.create(resourcename='Matplotlib', resourcetype='Library', resourceurl='https://matplotlib.org/', resourcedescription='Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible' )
      
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresource'))
        self.assertRedirects(response,'accounts/login/?next=/Club/newresource/')