from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_texture, name='redirect_to_texture'),
    path('earthtexture', views.follow_dragon_earthtexture_view, name='follow_dragon_earthtexture'),
    path('earthmap', views.follow_dragon_earthmap_view, name='follow_dragon_earthmap'),
    path('dragon_public.json', views.dragon_public, name='dragon_public'),
]
