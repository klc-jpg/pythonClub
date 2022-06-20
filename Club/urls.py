from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='index'),
   path('resources/', views.resources_view, name='resources'),
   path('meetings/', views.meetings_view, name='meetings'),
   path('meeting_minutes/<int:id>/', views.meeting_detail, name='details'),
   path('new_meeting/', views.new_meeting, name='newmeeting'),
   path('new_resource/', views.new_resource, name='newresource'),
   path('loginmessage/', views.login_message, name='login_message'),
   path('logoutmessage/', views.logout_message, name='logout_message'),
]