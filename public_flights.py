import requests
import time

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
PAGE_LIMIT = 20


def get_public_flights() -> tuple[list, list]:
    start_time = time.time()
    page_number = 0
    departures_list, arrivals_list = [], []
    previous_main_flight = ""
    while page_number < PAGE_LIMIT:
        params = {
            'page': f'{page_number}'
        }

        try:
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
                    
                    city_name_from_airport_code_url = PUBLIC_FLIGHTS_DESTINATIONS_URL + (flight['route'])['destinations'][0]
                    response = requests.get(url=city_name_from_airport_code_url, headers=HEADERS)

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
        except Exception as e:
            departures_list.append({None})
            arrivals_list.append({None})
            break

        page_number += 1

    print(f'Execution time: {round(time.time() - start_time, 2)} seconds')
    return (departures_list, arrivals_list)