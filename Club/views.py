from contextlib import contextmanager
from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event 
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def resources_view(request):
    resource_list=Resource.objects.all()
    return render(request, 'Club/resources.html', {'resource_list': resource_list})

def meetings_view(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'Club/meetings.html', {'meeting_list': meeting_list})

#def meeting_detail(request, id):
    #details=get_object_or_404(Meeting, pk=id)
    #return render(request, 'Club/meeting_minutes.html', {'details': details})

def meeting_detail(request, id):
    details=get_object_or_404(Meeting, pk=id)
    attendance=MeetingMinutes.objects.only("meetingid", "minutestext").only("attendance")
    context={
        'details': details,
        'attendance': attendance,
    }
    return render(request, 'Club/meeting_minutes.html',context=context)






