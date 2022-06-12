from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='index'),
   path('resources/', views.resources_view, name='resources'),
   path('meetings/', views.meetings_view, name='meetings'),
   path('meeting_minutes/<int:id>/', views.meeting_detail, name='details'),
]