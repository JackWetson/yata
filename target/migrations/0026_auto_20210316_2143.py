# Generated by Django 3.1.5 on 2021-03-16 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0025_auto_20210223_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attack',
            old_name='baseRespect',
            new_name='base_respect',
        ),
        migrations.RenameField(
            model_name='attack',
            old_name='chainBonus',
            new_name='chain_bonus',
        ),
        migrations.RenameField(
            model_name='attack',
            old_name='fairFight',
            new_name='fair_fight',
        ),
        migrations.RenameField(
            model_name='attack',
            old_name='flatRespect',
            new_name='flat_respect',
        ),
        migrations.RenameField(
            model_name='attack',
            old_name='groupAttack',
            new_name='group_attack',
        ),
        migrations.RenameField(
            model_name='targetinfo',
            old_name='baseRespect',
            new_name='base_respect',
        ),
        migrations.RenameField(
            model_name='targetinfo',
            old_name='fairFight',
            new_name='fair_fight',
        ),
        migrations.RenameField(
            model_name='targetinfo',
            old_name='flatRespect',
            new_name='flat_respect',
        ),
    ]
