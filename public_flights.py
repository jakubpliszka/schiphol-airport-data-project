from website_project.models import ArrivalFlight, DepartureFlight

import requests
import time

from datetime import datetime

APP_ID = ''
APP_KEY = ''
HEADERS = {
    'accept': 'application/json',
    'resourceversion': 'v4',
    'app_id': APP_ID,
    'app_key': APP_KEY
}

PUBLIC_FLIGHTS_URL = 'https://api.schiphol.nl/public-flights/flights'
PUBLIC_FLIGHTS_DESTINATIONS_URL = 'https://api.schiphol.nl/public-flights/destinations/'
PAGE_LIMIT = 200


def get_public_flights() -> tuple[list, list]:
    start_time = time.time()
    page_number = 0
    departures_list, arrivals_list = [], []
    previous_main_flight = ""
    while page_number < PAGE_LIMIT:
        params = {
            'page': f'{page_number}'
        }

        # try:
        response = requests.get(url=PUBLIC_FLIGHTS_URL, headers=HEADERS, params=params)
        if response.status_code != 200:
            departures_list.append({None})
            arrivals_list.append({None})
            break
        else:
            flights = response.json()
            if not flights['flights']:
                break
            
            for flight in flights['flights']:
                if flight['mainFlight'] == previous_main_flight:
                    continue
                
                # city_name_from_airport_code_url = PUBLIC_FLIGHTS_DESTINATIONS_URL + (flight['route'])['destinations'][0]
                # response = requests.get(url=city_name_from_airport_code_url, headers=HEADERS)

                # if response.status_code != 200:
                #     city_name = (flight['route'])['destinations'][0]
                #     print(response)
                # else:
                #     city_name_json = response.json()
                #     city_name = city_name_json['city']

                city_name = (flight['route'])['destinations'][0]
                temp_dict = {
                    'flightName': flight['mainFlight'],
                    'scheduleDate': flight['scheduleDate'],
                    'scheduleTime': flight['scheduleTime'],
                    'flightDirection': f"{city_name}",
                    'aircraftType': (flight['aircraftType'])['iataSub']
                }

                formatted_date = datetime.strptime(flight['scheduleDate'], '%Y-%m-%d').date()   # convert flight date to match models time format
                formatted_time = datetime.strptime(flight['scheduleTime'], '%H:%M:%S').time()   # convert flight time to match models time format

                if flight['flightDirection'].lower() == "d":
                    register_departure_flight = DepartureFlight(flight_number = flight['mainFlight'],
                                                                flight_date = formatted_date,
                                                                flight_time = formatted_time,
                                                                flight_direction = city_name,
                                                                aircraft_type = (flight['aircraftType'])['iataSub'])
                    register_departure_flight.save()
                    departures_list.append(temp_dict)
                elif flight['flightDirection'].lower() == "a":
                    register_arrival_flight = ArrivalFlight(flight_number = flight['mainFlight'],
                                                            flight_date = formatted_date,
                                                            flight_time = formatted_time,
                                                            flight_direction = city_name,
                                                            aircraft_type = (flight['aircraftType'])['iataSub'])
                    register_arrival_flight.save()
                    arrivals_list.append(temp_dict)

                previous_main_flight = flight['mainFlight']
        # except Exception as error:
        #     print("Caught exception!", error)
        #     departures_list.append({None})
        #     arrivals_list.append({None})
        #     break

        page_number += 1

    print(f'Execution time: {round(time.time() - start_time, 2)} seconds')
    return (departures_list, arrivals_list)