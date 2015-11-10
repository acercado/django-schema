# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('schedule', models.CharField(blank=True, null=True, max_length=200)),
                ('billingpostalcode', models.CharField(blank=True, null=True, max_length=20)),
                ('isdeleted', models.BooleanField(default=False)),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('billinglatitude', models.DecimalField(decimal_places=8, blank=True, null=True, max_digits=11)),
                ('_hc_lastop', models.CharField(blank=True, null=True, max_length=32)),
                ('createddate', models.DateTimeField(blank=True, null=True)),
                ('billingcountry', models.CharField(blank=True, null=True, max_length=80)),
                ('geolocation_longitude_s', models.DecimalField(decimal_places=8, blank=True, null=True, db_column='geolocation__longitude__s', max_digits=11)),
                ('geolocation_latitude_s', models.DecimalField(decimal_places=8, blank=True, null=True, db_column='geolocation__latitude__s', max_digits=11)),
                ('billingstate', models.CharField(blank=True, null=True, max_length=80)),
                ('billingstreet', models.CharField(blank=True, null=True, max_length=255)),
                ('billinglongitude', models.DecimalField(decimal_places=8, blank=True, null=True, max_digits=11)),
                ('billingcity', models.CharField(blank=True, null=True, max_length=40)),
                ('systemmodstamp', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, null=True, max_length=255)),
                ('_hc_err', models.TextField(blank=True, null=True)),
                ('sfid', models.CharField(blank=True, null=True, max_length=18)),
                ('is_featured', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Salesforce Accounts',
                'db_table': 'salesforce"."account',
                'verbose_name': 'Salesforce Account',
                'managed': True,
            },
        ),
    ]
