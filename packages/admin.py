from django.contrib import admin
from . models import Packages,ItineraryItem,UmrahPackage_Details
# Register your models here.

admin.site.register(Packages)
admin.site.register(ItineraryItem)
admin.site.register(UmrahPackage_Details)

