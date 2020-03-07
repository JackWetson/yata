# Generated by Django 2.0.7 on 2020-03-05 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0038_auto_20200305_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='crimesChannels',
            field=models.CharField(blank=True, default='["oc"]', help_text='Name of the channels where OC commands are allowed. Keep ["*"] for all channels allowed. It has to be the exact channel name: ["channel-a", "my-other-channel"]', max_length=64),
        ),
    ]