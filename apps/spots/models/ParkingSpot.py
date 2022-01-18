from django.db import models


class PublicParkingspot(models.Model):
    spotid = models.AutoField(db_column='spotId', primary_key=True)  # Field name made lowercase.
    spotlong = models.DecimalField(db_column='spotLong', max_digits=18, decimal_places=16)  # Field name made lowercase.
    spotlat = models.DecimalField(db_column='spotLat', max_digits=18, decimal_places=16)  # Field name made lowercase.
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    categoryspot = models.CharField(db_column='categorySpot', max_length=20)  # Field name made lowercase.
    catid = models.ForeignKey('PublicCatparking', models.DO_NOTHING, db_column='catId')  # Field name made lowercase.