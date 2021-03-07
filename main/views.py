from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'main/home.htm')

def updates(request):
    return render(request, 'main/updates.htm')
# Create your views here.
