"""webplayground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from pages.urls import pages_patterns
from profiles.urls import profiles_patterns
from blog.urls import blog_patterns
from messenger.urls import messenger_patterns
from about.urls import about_patterns
from portfolio.urls import portfolio_patterns
from services.urls import services_patterns
from contact.urls import contact_patterns

urlpatterns = [
        path('admin/', admin.site.urls),
        path('paginas/', include(pages_patterns)),
        path('', include('core.urls')),

        #Paths de auth
        # path('registro/', include(register_pattern)),
        path('cuentas/', include('django.contrib.auth.urls')),
        path('registro/', include('registration.urls')),

        path('equipo/', include(profiles_patterns)),

        #Paths de messenger
        path('messenger/', include(messenger_patterns)),

        #   Path para el blog
        path('blog/', include(blog_patterns)),

        #   Path para acerca de nosotros
        path('acerca-de-nosotros/', include(about_patterns)),

        #   Path para Portfolio
        path('portafolio/', include(portfolio_patterns)),

        #   Path para los servicios
        path('servicios/', include(services_patterns)),
    
        #   Path para la seccion de contactos
        path('contacto/', include(contact_patterns))
]

#Haciendo posible poder guardar imagenes localmente, es necesario tener el mode DEBUG en True en Settings.py
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        