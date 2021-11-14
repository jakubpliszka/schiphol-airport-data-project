from django.contrib import admin

from website_project.models import ArrivalFlight, DepartureFlight
# Register your models here.

admin.site.register(DepartureFlight)
admin.site.register(ArrivalFlight)