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
