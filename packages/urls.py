from django.urls import path
from . import views

urlpatterns = [
   path('packages/', views.view_packages, name='packages'),
   path('package_details/<int:pk>/', views.package_details, name='package_details'),
   path('umrah_details/', views.umrah_package_details, name='umrah_details')
]  