

# Create your models here.
from django.db import models

class doners_details(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    donation_date = models.DateField()
    

    def __str__(self):
        return "%s %s" %(self.first_name,self.last_name)
