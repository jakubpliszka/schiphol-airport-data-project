from datetime import datetime, timedelta

from website_project.models import ArrivalFlight, DepartureFlight


def get_flights_by_date():
    today = datetime.now().date()
    current_time = datetime.now().time()

    time_delta = timedelta(hours=-1)
    delta_time_back_from_now = (datetime.combine(today, current_time) + time_delta).time()

    # get all flights with today's date and flight time starting 1 hour back from now
    instance = DepartureFlight.objects.filter(flight_date=today, flight_time__gte=delta_time_back_from_now)
    print(instance.count())