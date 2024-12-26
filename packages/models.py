from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.



class Packages(models.Model):
    image = CloudinaryField('image', default='default_image_placeholder')
    sub_image_1 = CloudinaryField('image', default='default_image_placeholder')
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




class UmrahPackage_Details(models.Model):
    # General Information
    title = models.CharField(max_length=255, help_text="Title of the Umrah Package")
    description = models.TextField(help_text="Brief overview of the package")
    hero_image = CloudinaryField('image')

    # Highlights
    highlights = models.JSONField(default=list)

    # Package Details
    duration = models.CharField(max_length=100, help_text="Duration of the package (e.g., '7 days, 6 nights')")
    departure_date = models.DateField(help_text="Departure date for the package")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per person for the package")

    def get_highlights_list(self):
        """Convert highlights string to a list for easy iteration in the template."""
        return self.highlights.split(',')

    def __str__(self):
        return self.title


