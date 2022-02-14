from django.shortcuts import render
from django.http import HttpResponse

from flights_manage import get_flights_by_date, get_destinations_full_name
from data_analysis import create_plot_from_todays_flights


def index(request):
    return render(request, 'index.html')

def airport(request):
    get_destinations_full_name()
    departures, arrivals = get_flights_by_date()
    return render(request, 'airport.html', {'departures': departures, 'arrivals': arrivals})

def destinations(request):
    all_time_data = create_plot_from_todays_flights(get_all_time_data=True)
    todays_data = create_plot_from_todays_flights(get_all_time_data=False)
    return render(request, 'destinations.html', {'graph_all_data': all_time_data, 'graph_single_day': todays_data})

def aircrafts(request):
    return render(request, 'aircrafts.html')
