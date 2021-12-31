from django.contrib import admin

from website_project.models import ArrivalFlight, DepartureFlight, Destination
# Register your models here.

admin.site.register(DepartureFlight)
admin.site.register(ArrivalFlight)
admin.site.register(Destination)
