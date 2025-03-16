from django.urls import path
from . import views

urlpatterns = [
    path('', views.follow_dragon_earthtexture_view, name='follow_dragon_earthtexture_view'),
    # path('t', views.follow_dragon_earthtexture_view, name='follow_dragon_earthtexture'),
    # path('m', views.follow_dragon_earthmap_view, name='follow_dragon_earthmap'),
    path('dragon_public.json', views.dragon_public, name='dragon_public'),
]
