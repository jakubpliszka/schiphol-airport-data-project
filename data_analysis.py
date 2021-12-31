import matplotlib.pyplot as plot
from datetime import datetime
from io import StringIO

from website_project.models import Destination, DepartureFlight

ALL_COUNTRIES = {}
    

def count_flights_based_on_destination() -> None:
    """
    brief: this function gets all destinations from one day and counts number of flights to them
    return: dictionary of countries with value of how many flights where there
    """
    today = datetime.now().date()
    departures = DepartureFlight.objects.filter(flight_date=today)
            
    for flight in departures:
        city = flight.flight_direction
        destination = Destination.objects.filter(city=city).first()
        country = destination.country

        if country in ALL_COUNTRIES.keys():
            ALL_COUNTRIES[country] += 1
        else:
            ALL_COUNTRIES[country] = 1
    
def create_plot_from_todays_flights() -> list:
    count_flights_based_on_destination()

    if ALL_COUNTRIES == {}:
        return

    all_countries_sorted = {key: value for key, value in sorted(ALL_COUNTRIES.items(), key=lambda item: item[1], reverse=True)}
    
    figure = plot.figure(figsize=(20, 10))
    plot.bar(all_countries_sorted.keys(), all_countries_sorted.values(), align='edge', width=0.5)
    plot.xticks(rotation='vertical')
    imageData = StringIO()
    figure.savefig(imageData, format='svg')
    imageData.seek(0)

    data = imageData.getvalue()
    return data
