from django.db import models

# Create your models here.

class Contact(models.Model):
    contact_title = models.CharField(max_length=100)
    contact_sub_title = models.TextField(null=True)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=26)
    location = models.TextField(null=True)

    

    def __str__(self):
        return self.contact_title
