from django.urls import path
from .views import MainPage, ChatbotPage

services_patterns = ([
    path('', MainPage.as_view(), name='services-main'),
    path('chatbot/', ChatbotPage.as_view(), name='services-chatbot' )
], "services")
