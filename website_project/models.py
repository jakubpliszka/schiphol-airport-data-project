from django.db import models

# Create your models here.

class DepartureFlight(models.Model):
    flight_number = models.CharField(max_length=10)
    flight_date = models.DateField(max_length=10)
    flight_time = models.TimeField(max_length=8)
    flight_direction = models.CharField(max_length=100)
    aircraft_type = models.CharField(max_length=4)

class ArrivalFlight(models.Model):
    flight_number = models.CharField(max_length=10)
    flight_date = models.DateField(max_length=10)
    flight_time = models.TimeField(max_length=8)
    flight_direction = models.CharField(max_length=100)
    aircraft_type = models.CharField(max_length=4)

class DestinationCityName(models.Model):
    city = models.CharField(max_length=100)
    iata = models.CharField(max_length=4)
