from django.db import models

# Create your models here.


class House(models.Model):

    HOME_TYPE_CHOICES = [
        ('SingleFamily','Single Family'),
        ('VacantResidentialLand','Vacant Residential Land'),
        ('Miscellaneous','Miscellaneous'),
        ('MultiFamily2To4','Multi Family 2 to 4'),
        ('Condominium', 'Condominium'),
        ('Apartment','Apartment'),
        ('Duplex','Duplex')
    ]

    #System Generated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Data Fields
    area_unit = models.TextField(blank=True, null=True)
    bathrooms = models.FloatField(blank=True, null=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    home_size = models.IntegerField(blank=True, null=True)
    home_type = models.CharField(blank=True, null=True, max_length=50, choices=HOME_TYPE_CHOICES)
    last_sold_date = models.DateField(blank=True, null=True)
    last_sold_price = models.IntegerField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    property_size = models.IntegerField(blank=True, null=True)
    rent_price = models.IntegerField(blank=True, null=True)
    rentzestimate_amount = models.IntegerField(blank=True, null=True)
    rentzestimate_last_updated = models.DateField(blank=True, null=True)
    tax_value = models.FloatField(blank=True, null=True)
    tax_year = models.IntegerField(blank=True, null=True)
    year_built = models.IntegerField(blank=True, null=True)
    zestimate_amount = models.IntegerField(blank=True, null=True)
    zestimate_last_updated = models.DateField(blank=True, null=True)
    zillow_id = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    zipcode = models.CharField(blank=True, null=True, max_length=5)

