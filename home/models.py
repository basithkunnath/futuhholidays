from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Carsousel(models.Model):
    country_name = models.CharField(max_length=100)
    sub_destinations = models.CharField(max_length=100)
    image = CloudinaryField('image', default='default_image_placeholder')
    def __str__(self):
        return self.country_name


class Introduction(models.Model):
    logo_image_1 = CloudinaryField('image', default='default_image_placeholder')
    logo_image_2 = CloudinaryField('image', default='default_image_placeholder')
    welcome_title = models.CharField(max_length=100)
    welcome_paragraph = models.CharField(max_length=1000)
    

    def __str__(self):
        return self.welcome_title



class Whytravel(models.Model):
    whytravel_title = models.CharField(max_length=100)
    feature_one = models.CharField(max_length=300)
    feature_two = models.CharField(max_length=300)
    feature_three = models.CharField(max_length=300)
    feature_four = models.CharField(max_length=300)
    

    def __str__(self):
        return self.whytravel_title



class UpcomingTrips(models.Model):
    package_image = CloudinaryField('image', default='default_image_placeholder')
    package_title = models.CharField(max_length=100)
    package_shot_description = models.CharField(max_length=100)
  
    

    def __str__(self):
        return self.package_title


class UmrahPackage(models.Model):
    umrah_package_title = models.CharField(max_length=100)
    umrah_package_sub_title = models.CharField(max_length=100)
    umrah_package_short_description = models.TextField(null=True)
    umrah_package_free_text = models.CharField(max_length=100)
    umrah_package_bg_image = CloudinaryField('image', default='default_image_placeholder')
  
    

    def __str__(self):
        return self.umrah_package_title



class AboutSection(models.Model):
    about_title = models.CharField(max_length=100)
    about_first_paragraph = models.TextField(null=True)
    about_second_paragraph = models.TextField(null=True)
    about_image = CloudinaryField('image', default='default_image_placeholder')
    

    def __str__(self):
        return self.about_title




class Destinations(models.Model):
    destination_image = CloudinaryField('image', default='default_image_placeholder')
    destination_name = models.CharField(max_length=100)

    def __str__(self):
        return self.destination_name


