# Generated by Django 3.0.8 on 2020-08-15 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0093_faction_pj_pa_dump'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faction',
            name='pj_pa_Dump',
        ),
        migrations.AddField(
            model_name='faction',
            name='ph_pa_Dump',
            field=models.TextField(default='[]'),
        ),
        migrations.AlterField(
            model_name='faction',
            name='crimesDump',
            field=models.TextField(default='[]'),
        ),
        migrations.AlterField(
            model_name='faction',
            name='crimesRank',
            field=models.TextField(default='[]'),
        ),
    ]
