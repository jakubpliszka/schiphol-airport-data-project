from django.shortcuts import render
from django.http import HttpResponse

import requests

PUBLIC_FLIGHTS_URL = 'https://api.schiphol.nl/public-flights/flights'

# Create your views here.

def index(request):
    return render(request, 'index.html')

def airport(request):
    flights = get_public_flights()
    return render(request, 'airport.html', {'flights': flights})

def destinations(request):
    return render(request, 'destinations.html')

def aircrafts(request):
    return render(request, 'aircrafts.html')

def get_public_flights():
    app_id = ''
    app_key = ''

    header = {
      'accept': 'application/json',
	  'resourceversion': 'v4',
      'app_id': app_id,
	  'app_key': app_key
	}

    response = requests.request('GET', url=PUBLIC_FLIGHTS_URL, headers=header)
    if response.status_code == 200:
        flights = response.json()
    else:
        flights = {'flights': None}
    
    return flights['flights']