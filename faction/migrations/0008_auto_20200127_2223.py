# Generated by Django 3.0.1 on 2020-01-27 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0007_chain'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttackChain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tId', models.IntegerField(default=0)),
                ('timestamp_started', models.IntegerField(default=0)),
                ('timestamp_ended', models.IntegerField(default=0)),
                ('attacker_id', models.IntegerField(default=0)),
                ('attacker_name', models.CharField(blank=True, default='attacker_name', max_length=16, null=True)),
                ('attacker_faction', models.IntegerField(default=0)),
                ('attacker_factionname', models.CharField(blank=True, default='attacker_factionname', max_length=32, null=True)),
                ('defender_id', models.IntegerField(default=0)),
                ('defender_name', models.CharField(blank=True, default='defender_name', max_length=16, null=True)),
                ('defender_faction', models.IntegerField(default=0)),
                ('defender_factionname', models.CharField(blank=True, default='defender_factionname', max_length=32, null=True)),
                ('result', models.CharField(default='result', max_length=32)),
                ('stealthed', models.IntegerField(default=0)),
                ('respect_gain', models.FloatField(default=0.0)),
                ('chain', models.IntegerField(default=0)),
                ('fairFight', models.FloatField(default=0.0)),
                ('war', models.IntegerField(default=0)),
                ('retaliation', models.FloatField(default=0.0)),
                ('groupAttack', models.FloatField(default=0.0)),
                ('overseas', models.FloatField(default=0.0)),
                ('chainBonus', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='chain',
            name='combine',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chain',
            name='computing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chain',
            name='current',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='chain',
            name='graphs',
            field=models.TextField(blank=True, default='{}', null=True),
        ),
        migrations.AddField(
            model_name='chain',
            name='lastUpdate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='chain',
            name='live',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chain',
            name='report',
            field=models.BooleanField(default=False),
        ),
    ]
