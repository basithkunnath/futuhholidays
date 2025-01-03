"""
URL configuration for futuhtravels project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),         # Admin site
    path('', include('home.urls')),          # Root URL for the home app
    path('about/', include('about.urls')),   # URL prefix for the about app
    path('packages/', include('packages.urls')), # URL prefix for the packages app
    path('gallery/', include('gallery.urls')),   # URL prefix for the gallery app
    path('contact/', include('contact.urls')),   # URL prefix for the contact app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
