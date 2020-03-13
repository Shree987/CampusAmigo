from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/',views.student,name='student'),
    path('student/club/',views.club,name='club'),
    path('student/event/',views.event,name='event'),
    
]