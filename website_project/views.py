from django.shortcuts import render
from django.http import HttpResponse

from flights_manage import get_flights_by_date
from public_flights import get_public_flights
# Create your views here.

def index(request):
    get_flights_by_date()
    return render(request, 'index.html')

def airport(request):
    departures_list, arrivals_list = get_public_flights()
    return render(request, 'airport.html', {'departures': departures_list, 'arrivals': arrivals_list})

def destinations(request):
    return render(request, 'destinations.html')

def aircrafts(request):
    return render(request, 'aircrafts.html')
