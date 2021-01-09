# Generated by Django 3.1.2 on 2020-12-27 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0014_dropletspec'),
    ]

    operations = [
        migrations.AddField(
            model_name='dropletspec',
            name='disk',
            field=models.CharField(default='disk', max_length=32),
        ),
        migrations.AddField(
            model_name='dropletspec',
            name='memory',
            field=models.CharField(default='memory', max_length=32),
        ),
        migrations.AddField(
            model_name='dropletspec',
            name='transfer',
            field=models.CharField(default='transfer', max_length=32),
        ),
        migrations.AddField(
            model_name='dropletspec',
            name='vcpu',
            field=models.CharField(default='vcpu', max_length=32),
        ),
        migrations.AlterField(
            model_name='dropletspec',
            name='name',
            field=models.CharField(default='name', max_length=32),
        ),
        migrations.AlterField(
            model_name='dropletspec',
            name='vpc_uuid',
            field=models.CharField(default='vpc_uuid', max_length=32),
        ),
    ]