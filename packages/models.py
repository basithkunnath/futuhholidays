from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.



class Packages(models.Model):
    image = CloudinaryField('image', default='default_image_placeholder')
    sub_image_2 = CloudinaryField('image', default='default_image_placeholder')
    title = models.CharField(max_length=100)
    short_description = models.TextField(null=True)
    country = models.CharField(max_length=100,default='Unknown Country')
    duration = models.CharField(max_length=100,default='Unknown Date')
    details_description = models.TextField(null=True)
    features = models.JSONField(default=list)
    
  
    def __str__(self):
        return self.title
    



class ItineraryItem(models.Model):
    package = models.ForeignKey(Packages, on_delete=models.CASCADE, related_name='itinerary_items')
    day_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"Day {self.day_number}: {self.title}"

