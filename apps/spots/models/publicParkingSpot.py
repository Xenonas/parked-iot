# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PublicParkingspot(models.Model):
    spotid = models.AutoField(db_column='spotId', primary_key=True)  # Field name made lowercase.
    spotlong = models.DecimalField(db_column='spotLong', max_digits=10, decimal_places=0)  # Field name made lowercase.
    spotlat = models.DecimalField(db_column='spotLat', max_digits=10, decimal_places=0)  # Field name made lowercase.
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    categoryspot = models.CharField(db_column='categorySpot', max_length=20)  # Field name made lowercase.
    catid = models.ForeignKey('PublicCatparking', models.DO_NOTHING, db_column='catId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'public.parkingSpot'
