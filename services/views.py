from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MainPage(TemplateView):
    template_name = "services/main.html"

class ChatbotPage(TemplateView):
    template_name = 'services/chatbot.html'