from django.shortcuts import render
from Club.models import Meeting, MeetingMinutes, Resource, Event 

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def resources_view(request):
    resource_list=Resource.objects.all()
    return render(request, "Club/resources.html", {'resource_list': resource_list})







