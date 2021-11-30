from django.shortcuts import render
from django.http import HttpResponse

from flights_manage import get_flights_by_date, get_destinations_full_name
# Create your views here.

def index(request):
    get_destinations_full_name()
    return render(request, 'index.html')

def airport(request):
    departures, arrivals = get_flights_by_date()
    return render(request, 'airport.html', {'departures': departures, 'arrivals': arrivals})

def destinations(request):
    return render(request, 'destinations.html')

def aircrafts(request):
    return render(request, 'aircrafts.html')
