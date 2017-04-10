# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class HomeData(models.Model):
    street_address = models.CharField(primary_key=True, max_length=255)
    zip = models.IntegerField()
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    home_type = models.CharField(max_length=255, blank=True, null=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.IntegerField(blank=True, null=True)
    finished_sq_footage = models.IntegerField(blank=True, null=True)
    lot_size_sq_footage = models.IntegerField(blank=True, null=True)
    year_built = models.IntegerField(blank=True, null=True)
    year_updated = models.IntegerField(blank=True, null=True)
    number_of_floors = models.IntegerField(blank=True, null=True)
    parking_type = models.CharField(max_length=255, blank=True, null=True)
    heating_sources = models.CharField(max_length=255, blank=True, null=True)
    heating_system = models.CharField(max_length=255, blank=True, null=True)
    floor_covering = models.CharField(max_length=255, blank=True, null=True)
    number_of_rooms = models.IntegerField(blank=True, null=True)
    neighborhood = models.CharField(max_length=255, blank=True, null=True)
    school_district = models.CharField(max_length=255, blank=True, null=True)
    sold_binary = models.IntegerField()
    last_sold_date = models.CharField(max_length=255, blank=True, null=True)
    last_sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    appliances = models.CharField(max_length=500, blank=True, null=True)
    roof_type = models.CharField(max_length=255, blank=True, null=True)
    room_types = models.CharField(max_length=500, blank=True, null=True)
    updated_properties = models.IntegerField()
    price_range = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_data'
