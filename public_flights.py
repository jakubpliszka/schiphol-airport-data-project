import requests
import time

from datetime import datetime

# from requests.api import get

from website_project.models import ArrivalFlight, DepartureFlight, Destination

APP_ID = ''
APP_KEY = ''
HEADERS = {
    'accept': 'application/json',
    'resourceversion': 'v4',
    'app_id': APP_ID,
    'app_key': APP_KEY
}

PUBLIC_FLIGHTS_URL = 'https://api.schiphol.nl/public-flights/flights'
PUBLIC_FLIGHTS_DESTINATIONS_URL = 'https://api.schiphol.nl/public-flights/destinations'
PAGE_LIMIT = 999


def get_destinations_from_api() -> bool:
    page_number = 0
    
    while page_number < PAGE_LIMIT:
        params = {
            'page': f'{page_number}'
        }
        try:
            response = requests.get(url=PUBLIC_FLIGHTS_DESTINATIONS_URL, headers=HEADERS, params=params)
            if response.status_code != 200:
                print(response)
            else:
                destinations = response.json()
                if not destinations['destinations']:
                    return True

                for destination in destinations['destinations']:
                    city = destination['city'] if destination['city'] is not None else "N/A"
                    iata = destination['iata'] if destination['iata'] is not None else "N/A"
                    country = destination['country'] if destination['country'] is not None else "N/A"

                    register_destination = Destination(city=city, iata=iata, country=country)
                    register_destination.save()
        except Exception as error:
            print("Caught exception!", error)
            return False

        page_number += 1

    return True

def get_public_flights_from_api() -> bool:
    start_time = time.time()
    page_number = 0
    previous_main_flight = ""
    while page_number < PAGE_LIMIT:
        params = {
            'page': f'{page_number}'
        }

        try:
            response = requests.get(url=PUBLIC_FLIGHTS_URL, headers=HEADERS, params=params)
            if response.status_code != 200:
                print(response)
            else:
                flights = response.json()
                if not flights['flights']:
                    return True
                
                for flight in flights['flights']:
                    if flight['mainFlight'] == previous_main_flight:
                        continue
                    
                    flight_number = flight['mainFlight'] if flight['mainFlight'] is not None else "N/A"
                    formatted_date = datetime.strptime(flight['scheduleDate'], '%Y-%m-%d').date() if flight['scheduleDate'] is not None else "N/A"  # convert flight date to match models time format
                    formatted_time = datetime.strptime(flight['scheduleTime'], '%H:%M:%S').time() if flight['scheduleTime'] is not None else "N/A"  # convert flight time to match models time format
                    city_model = Destination.objects.get(iata=flight['route']['destinations'][0])
                    if city_model.city is not None:
                        flight_direction = city_model.city
                    elif flight['route']['destinations'][0] is not None:
                        flight_direction = flight['route']['destinations'][0]
                    else:
                        flight_direction = "N/A"
                    aircraft_type = flight['aircraftType']['iataSub'] if flight['aircraftType']['iataSub'] is not None else "N/A"

                    if flight['flightDirection'].lower() == "d":
                        register_departure_flight = DepartureFlight(flight_number = flight_number,
                                                                    flight_date = formatted_date,
                                                                    flight_time = formatted_time,
                                                                    flight_direction = flight_direction,
                                                                    aircraft_type = aircraft_type)
                        register_departure_flight.save()
                    elif flight['flightDirection'].lower() == "a":
                        register_arrival_flight = ArrivalFlight(flight_number = flight_number,
                                                                flight_date = formatted_date,
                                                                flight_time = formatted_time,
                                                                flight_direction = flight_direction,
                                                                aircraft_type = aircraft_type)
                        register_arrival_flight.save()

                    previous_main_flight = flight['mainFlight']
        except Exception as error:
            print("Caught exception!", error)
            return False

        page_number += 1

    print(f'Execution time: {round(time.time() - start_time, 2)} seconds')
    return True
