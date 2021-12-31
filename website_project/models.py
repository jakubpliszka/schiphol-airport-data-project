from django.db import models

# Create your models here.

class DepartureFlight(models.Model):
    flight_number = models.CharField(max_length=10, default="N/A")
    flight_date = models.DateField(max_length=10, default="N/A")
    flight_time = models.TimeField(max_length=8, default="N/A")
    flight_direction = models.CharField(max_length=100, default="N/A")
    aircraft_type = models.CharField(max_length=4, default="N/A")

class ArrivalFlight(models.Model):
    flight_number = models.CharField(max_length=10, default="N/A")
    flight_date = models.DateField(max_length=10, default="N/A")
    flight_time = models.TimeField(max_length=8, default="N/A")
    flight_direction = models.CharField(max_length=100, default="N/A")
    aircraft_type = models.CharField(max_length=4, default="N/A")

class Destination(models.Model):
    city = models.CharField(max_length=100, default="N/A")
    iata = models.CharField(max_length=4, default="N/A")
    country = models.CharField(max_length=100, default="N/A")
