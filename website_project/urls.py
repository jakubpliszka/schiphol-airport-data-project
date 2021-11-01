from django.urls import path
from website_project import views

urlpatterns = [
    path('', views.index, name='index'),
    path('graphs', views.graphs, name='graphs'),
    path('destinations', views.destinations, name='destinations'),
    path('aircrafts', views.aircrafts, name='aricrafts'),
]
