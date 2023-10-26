from django.urls import path
from .views import MainPage

services_patterns = ([
    path('', MainPage.as_view(), name='services-main')
], "services")
