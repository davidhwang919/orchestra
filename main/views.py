from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
def home(request):
    return render(request, 'main/home.htm')

def updates(request):
    projects = Project.objects.all()
    return render(request, 'main/updates.htm', {'projects':projects})
# Create your views here.

def about(request):
    return render(request, 'main/about.htm')

def danny(request):
    return render(request, 'main/danny.htm')


def test(request):
    return render(request, 'main/test.htm')


def band(request):
    return render(request, 'main/band.htm')

def raid(request):
    return render(request, 'main/raid.htm')


def throne(request):
    return render(request, 'main/throne.htm')

    
def eine(request):
    return render(request, 'main/eine.htm')

def recent(request):
    return render(request, 'main/recent.htm')

def past(request):
    return render(request, 'main/past.htm')