from django.contrib import admin
from . models import Carsousel
from . models import Introduction
from . models import Whytravel
from . models import UpcomingTrips
from . models import UmrahPackage
from . models import AboutSection
from . models import Destinations
from .models import PopupImage


# Register your models here.
admin.site.register(Carsousel)
admin.site.register(Introduction)
admin.site.register(Whytravel)
admin.site.register(UpcomingTrips)
admin.site.register(UmrahPackage)
admin.site.register(AboutSection)
admin.site.register(Destinations)


@admin.register(PopupImage)
class PopupImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
