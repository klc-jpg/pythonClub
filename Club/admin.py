from django.contrib import admin
from .models import Meeting, MeetingMinutes, Resource, EventOne

# Register your models here.
admin.site.register(Meeting)
admin.site.register(MeetingMinutes)
admin.site.register(Resource)
admin.site.register(EventOne)