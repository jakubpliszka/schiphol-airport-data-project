from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def graphs(request):
    return render(request, 'graphs.html')

def destinations(request):
    return render(request, 'destinations.html')

def aircrafts(request):
    return render(request, 'aircrafts.html')