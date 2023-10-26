from django.urls import path
from .views import ContactView

contact_patterns = ([
    path('', ContactView, name="contact-us")
], 'contact')