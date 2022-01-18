from django.db import models


class Catparking(models.Model):
    dmslong = models.DecimalField(db_column='dmsLong', max_digits=18, decimal_places=16)  # Field name made lowercase.
    dmslat = models.DecimalField(db_column='dmsLat', max_digits=18, decimal_places=16)  # Field name made lowercase.
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    categoryparking = models.CharField(db_column='categoryParking', max_length=10)  # Field name made lowercase.
    allowedvehicletype = models.CharField(db_column='allowedVehicleType', max_length=20)  # Field name made lowercase.
    totalspotnumber = models.IntegerField(db_column='totalSpotNumber')  # Field name made lowercase.
    timemodified = models.DateTimeField(db_column='timeModified', auto_now=True)  # Field name made lowercase.
    address = models.CharField(max_length=100)
    requiredpermit = models.CharField(db_column='requiredPermit', max_length=50)  # Field name made lowercase.
    orgid = models.ForeignKey('PublicOrganization', models.DO_NOTHING, db_column='orgId')  # Field name made lowercase.