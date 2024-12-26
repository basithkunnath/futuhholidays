from django.shortcuts import render

# Create your views here.

# views.py
from django.shortcuts import render
from .models import Carsousel
from .models import Introduction
from .models import Whytravel
from .models import UpcomingTrips
from .models import UmrahPackage
from .models import AboutSection
from .models import Destinations
from .models import PopupImage
from about . models import Testimonial


def carsousel_view(request):
    view_carsousel = Carsousel.objects.all()
    view_introduction = Introduction.objects.first()
    view_whytravel = Whytravel.objects.first
    list_upcomingtrips = UpcomingTrips.objects.all()
    display_umrah_banner = UmrahPackage.objects.first()
    view_about_section = AboutSection.objects.first()
    view_destinations = Destinations.objects.all()
    view_testimonial = Testimonial.objects.all()
    popup_image = PopupImage.objects.last()  # Fetch the most recent image
    context = {
        'view_carsousel': view_carsousel,
        'view_introduction':view_introduction,
        'view_whytravel': view_whytravel,
        'list_upcoming_trips': list_upcomingtrips,
        'display_umrah_banner':display_umrah_banner,
        'view_about_section':view_about_section,
        'view_destinations' :view_destinations,
        'view_testimonial': view_testimonial,
        'popup_image': popup_image
        
    }
    return render(request, 'index.html', context)
