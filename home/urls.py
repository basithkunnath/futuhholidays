from django.urls import path
from . import views
urlpatterns = [
    path('', views.carsousel_view, name='home'),
]


