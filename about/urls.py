from django.urls import path
from .views import AboutView

about_patterns = ([
    path('', AboutView, name="about-page")
], 'about')