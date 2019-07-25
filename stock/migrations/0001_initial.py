# Generated by Django 2.0.7 on 2019-07-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tId', models.IntegerField(default=0, unique=True)),
                ('tName', models.CharField(default='tName', max_length=200)),
                ('tAcronym', models.CharField(default='tAcronym', max_length=10)),
                ('tDirector', models.CharField(default='tDirector', max_length=20)),
                ('tCurrentPrice', models.FloatField(default=0.0)),
                ('tMarketCap', models.IntegerField(default=0)),
                ('tTotalShares', models.IntegerField(default=0)),
                ('tAvailableShares', models.IntegerField(default=0)),
                ('tForecast', models.CharField(default='tForecast', max_length=20)),
                ('tDemand', models.CharField(default='tDemand', max_length=20)),
                ('tRequirement', models.IntegerField(default=0)),
                ('tDescription', models.CharField(blank=True, default='tDescription', max_length=20)),
                ('timestamp', models.IntegerField(default=0)),
            ],
        ),
    ]