from django.shortcuts import render
from .models import Gallery
# Create your views here.


def gallery(request):
    view_gallery = Gallery.objects.all()
    context = {
        'list_gallery_img': view_gallery
    }
    return render(request, 'gallery.html',context)