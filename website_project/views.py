from django.shortcuts import render
from django.http import HttpResponse

import requests

APP_ID = ''
APP_KEY = ''
PUBLIC_FLIGHTS_URL = 'https://api.schiphol.nl/public-flights/flights'
PUBLIC_FLIGHTS_DESTINATIONS_URL = 'https://api.schiphol.nl/public-flights/destinations/'
PAGE_LIMIT = 5

# Create your views here.

def index(request):
    return render(request, 'index.html')

def airport(request):
    departures_list, arrivals_list = get_public_flights()
    return render(request, 'airport.html', {'departures': departures_list, 'arrivals': arrivals_list})

def destinations(request):
    return render(request, 'destinations.html')

def aircrafts(request):
    return render(request, 'aircrafts.html')

def get_public_flights():
    headers = {
      'accept': 'application/json',
	  'resourceversion': 'v4',
      'app_id': APP_ID,
	  'app_key': APP_KEY
	}
    
    page_number = 0
    departures_list, arrivals_list = [], []
    previous_main_flight = ""

    while True:
        params = {
            'page': f'{page_number}'
        }

        response = requests.get(url=PUBLIC_FLIGHTS_URL, headers=headers, params=params)
        if response.status_code == 200:
            flights = response.json()
            if not flights['flights'] or page_number == PAGE_LIMIT:
                break
            
            for flight in flights['flights']:
                if flight['mainFlight'] == previous_main_flight:
                    continue
                
                city_name_from_airport_code_url = PUBLIC_FLIGHTS_DESTINATIONS_URL + (flight['route'])['destinations'][0]
                response = requests.get(url=city_name_from_airport_code_url, headers=headers)

                city_name_json = response.json()
                city_name = city_name_json['city']

                temp_dict = {
                    'flightName': flight['mainFlight'],
                    'scheduleDate': flight['scheduleDate'],
                    'scheduleTime': flight['scheduleTime'],
                    'flightDirection': f"{city_name}",
                    'aircraftType': (flight['aircraftType'])['iataSub']
                }
                if flight['flightDirection'].lower() == "d":
                    departures_list.append(temp_dict)
                elif flight['flightDirection'].lower() == "a":
                    arrivals_list.append(temp_dict)
                previous_main_flight = flight['mainFlight']

        else:
            departures_list.append({None})
            arrivals_list.append({None})
            break

        page_number += 1

    return departures_list, arrivals_list