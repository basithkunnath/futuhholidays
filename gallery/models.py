from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Gallery(models.Model):
    gallery_image = CloudinaryField('image', default='default_image_placeholder')
def __str__(self):
        return str(self.pk)