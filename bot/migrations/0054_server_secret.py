# Generated by Django 3.0.8 on 2020-07-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0053_stocks'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='secret',
            field=models.CharField(default='x', help_text='Secret key to access read only configurations', max_length=16),
        ),
    ]
