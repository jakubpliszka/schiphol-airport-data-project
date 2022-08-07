from datetime import datetime, timedelta

from src.public_flights import get_public_flights_from_api, get_destinations_from_api
from website_project.models import ArrivalFlight, DepartureFlight, Destination

TIME_DELTA = timedelta(hours=-1)
DATE_DELTA = timedelta(days=-1)


def get_destinations_full_name() -> bool:
    get_destinations = True
    if not Destination.objects.filter().exists():
        get_destinations = get_destinations_from_api()

    return get_destinations


def get_flights_by_date():
    today = datetime.now().date()
    current_time = datetime.now().time()

    delta_time_back_from_now = (datetime.combine(today, current_time) + TIME_DELTA).time()
    yesterday = (datetime.combine(today, current_time) + DATE_DELTA).date()

    is_todays_data = True
    # if there aren't objects with today's date, get api data
    if not DepartureFlight.objects.filter(flight_date=today).exists():
        is_todays_data = get_public_flights_from_api()

    if is_todays_data:
        # get all flights with today's date and flight time starting 1 hour back from now
        departures = DepartureFlight.objects.filter(flight_date=today, flight_time__gte=delta_time_back_from_now)
        arrivals = ArrivalFlight.objects.filter(flight_date=today, flight_time__gte=delta_time_back_from_now)
    else:
        # get all flights from yesterday instead
        departures = DepartureFlight.objects.filter(flight_date=yesterday)
        arrivals = ArrivalFlight.objects.filter(flight_date=yesterday)

    return (departures, arrivals)
