import matplotlib.pyplot as plot
from datetime import datetime
from io import StringIO

from website_project.models import Destination, DepartureFlight

    

def count_flights_based_on_destination(get_all_time_data : bool) -> dict:
    """
    @brief: this function gets all destinations from one todays's and counts number of flights to them
    @return: dictionary of countries with value of how many flights where there
    """
    if get_all_time_data:
        departures = DepartureFlight.objects.all()
    else:
        today = datetime.now().date()
        departures = DepartureFlight.objects.filter(flight_date=today)
            
    all_countries = {}
    for flight in departures:
        city = flight.flight_direction
        destination = Destination.objects.filter(city=city).first()
        country = destination.country

        if country in all_countries.keys():
            all_countries[country] += 1
        else:
            all_countries[country] = 1

    return all_countries
    
def create_plot_from_todays_flights(get_all_time_data : bool):
    """
    @brief: creates a plot from disctionary of counties with number of flights done
    @return:
    """
    all_counties = count_flights_based_on_destination(get_all_time_data=get_all_time_data)

    if not all_counties:   # if is empty
        return None

    # sort dictionary by number of flights done in descending order
    all_countries_sorted = {key: value for key, value in sorted(all_counties.items(), key=lambda item: item[1], reverse=True)}
    
    plot.figure(figsize=(15, 8))
    plot.bar(all_countries_sorted.keys(), all_countries_sorted.values(), align='edge', width=0.5)
    plot.xticks(rotation='vertical')
    # plot.savefig('graph.png')
    imageData = StringIO()
    plot.savefig(imageData, format='svg')
    imageData.seek(0)

    data = imageData.getvalue()
    return data
