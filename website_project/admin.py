from django.contrib import admin

from website_project.models import ArrivalFlight, DepartureFlight, DestinationCityName
# Register your models here.

admin.site.register(DepartureFlight)
admin.site.register(ArrivalFlight)
admin.site.register(DestinationCityName)
