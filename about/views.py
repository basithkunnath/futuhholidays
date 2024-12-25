from django.shortcuts import render
from .models import AboutPage
from .models import Testimonial
# Create your views here.


def about(request):
    view_aboutpage = AboutPage.objects.first
    view_testimonial = Testimonial.objects.all()
    context = {
        'view_aboutpage': view_aboutpage,
        'view_testimonial': view_testimonial
    }
    return render(request, 'about.html',context)

