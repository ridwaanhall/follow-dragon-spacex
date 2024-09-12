from django.urls import path
from . import views

urlpatterns = [
    path('text/', views.simple_text_view, name='simple_text_view'),
    path('json/', views.simple_json_view, name='simple_json_view'),
    path('no-content/', views.no_content_view, name='no_content_view'),
    path('redirect/', views.simple_redirect_view, name='simple_redirect_view'),
]
