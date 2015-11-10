from django.db import models

# Create your models here.

class Account(models.Model):
    schedule = models.CharField(max_length=200,null=True,blank=True)
    billingpostalcode = models.CharField(max_length=20, null=True, blank=True)
    isdeleted = models.BooleanField(default=False)
    id = models.IntegerField(primary_key=True)
    billinglatitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    _hc_lastop = models.CharField(max_length=32, null=True, blank=True)
    createddate = models.DateTimeField(null=True, blank=True)
    billingcountry = models.CharField(max_length=80, null=True, blank=True)
    geolocation_longitude_s = models.DecimalField(max_digits=11, decimal_places=8, db_column='geolocation__longitude__s', null=True, blank=True)
    geolocation_latitude_s = models.DecimalField(max_digits=11, decimal_places=8, db_column='geolocation__latitude__s', null=True, blank=True)
    billingstate = models.CharField(max_length=80, null=True, blank=True)
    billingstreet = models.CharField(max_length=255, null=True, blank=True)
    billinglongitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    billingcity = models.CharField(max_length=40, null=True, blank=True)
    systemmodstamp = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    _hc_err = models.TextField(null=True, blank=True)
    sfid = models.CharField(max_length=18, null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'salesforce\".\"account'
        verbose_name = 'Salesforce Account'
        verbose_name_plural = 'Salesforce Accounts'