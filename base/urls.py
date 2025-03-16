from django.urls import path
from . import views

urlpatterns = [
    path('', views.EarthMapView.as_view(), name='follow_dragon_earthmap_view'),
    path('dragon_public.json', views.DragonPublicView.as_view(), name='dragon_public'),
]
