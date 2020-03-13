from django.http import HttpResponse
from django.shortcuts import render
from .models import Student,Club,Event


def index(request):
    """View function for the home page of the site."""

    return render(request,'index.html')

def student(request):
    """View function for the student homepage."""

    student_name = Student.name

    return render(
        request,
        'student.html',
        context = {'student_name':student_name})

def club(request):
    """View for the clubs homepage."""

    club_name = Club.name
    about_us = Club.about_us
    convener = Club.convener

    return render(
        request,
        'club.html',
        context = {'club_name':club_name,'about_us':about_us,'convener':convener})

def event(request):
    """View for the events page."""

    event_name = Event.event_name
    club = Club.name
    description = Event.description
    date = Event.date
    time = Event.time
    venue = Event.venue

    return render(
        request,
        'event.html',
        context = {'event_name':event_name,'club':club,'description':description,
                   'date':date,'time':time,'venue':venue}
    )



