from django.urls import path
from . import views

urlpatterns = [
    path('', views.follow_dragon_view, name='follow_dragon'),
    path('dragon_public.json', views.dragon_public, name='dragon_public'),
]
