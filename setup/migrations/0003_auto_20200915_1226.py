# Generated by Django 3.1.1 on 2020-09-15 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0002_auto_20191029_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='key',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
