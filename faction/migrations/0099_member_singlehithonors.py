# Generated by Django 3.1.2 on 2020-12-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0098_merge_20201021_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='singleHitHonors',
            field=models.IntegerField(default=0),
        ),
    ]
