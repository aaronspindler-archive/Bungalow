from django.db import models

# Create your models here.

class House(models.Model):
    #System Generated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Data Fields
    area_unit = models.TextField(default='')
    bathrooms = models.FloatField(default=-1.0)
    bedrooms = models.FloatField(default=-1.0)
    home_size = models.IntegerField(default=-1)
    home_type = models.CharField(default='NA', max_length=50)
    last_sold_date = models.DateField()
    last_sold_price = models.IntegerField(default=-1)
    link = models.URLField()
    price = models.IntegerField(default=-1)
    rent_price = models.IntegerField(default=-1)
    rentzestimate_amount = models.IntegerField(default=-1)
    rentzestimate_last_updated = models.DateField()
    tax_value = models.FloatField(default=-1.0)
    tax_year = models.IntegerField(default=-1)
    year_built = models.IntegerField(default=-1)
    zestimate_amount = models.IntegerField(default=-1)
    zestimate_last_updated = models.DateField()
    zillow_id = models.IntegerField(default=-1)
    address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zipcode = models.CharField(max_length=11)

