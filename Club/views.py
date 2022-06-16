from contextlib import contextmanager
from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.utils import timezone
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import MeetingForm, ResourceForm

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def resources_view(request):
    resource_list=Resource.objects.all()
    return render(request, 'Club/resources.html', {'resource_list': resource_list})

def meetings_view(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'Club/meetings.html', {'meeting_list': meeting_list})

def meeting_detail(request, id):
    details=get_object_or_404(Meeting, pk=id)
    mins_list=MeetingMinutes.objects.all()
    users = User.objects.all()
    context={
        'details': details,
        'mins_list': mins_list,
        'users': users,  
    }
    return render(request, 'Club/meeting_minutes.html',context=context)

def new_meeting(request):
    form=MeetingForm 
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'Club/new_meeting.html', {'form': form}) 

def new_resource(request):
    form=ResourceForm 
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'Club/new_resource.html', {'form': form}) 


        
 