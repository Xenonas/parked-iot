from django.db import models


class PublicOrganization(models.Model):
    orgid = models.AutoField(db_column='orgId', primary_key=True)  # Field name made lowercase.
    orgname = models.CharField(db_column='orgName', max_length=50)  # Field name made lowercase.
    address = models.CharField(max_length=50)
    building = models.BooleanField()
    buildlat = models.DecimalField(db_column='buildLat', max_digits=18, decimal_places=16, blank=True, null=True)  # Field name made lowercase.
    buildlong = models.DecimalField(db_column='buildLong', max_digits=18, decimal_places=16, blank=True, null=True)  # Field name made lowercase.
    ramp = models.BooleanField(blank=True, null=True)