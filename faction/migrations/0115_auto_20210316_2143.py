# Generated by Django 3.1.5 on 2021-03-16 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0114_auto_20210223_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attackchain',
            old_name='chainBonus',
            new_name='chain_bonus',
        ),
        migrations.RenameField(
            model_name='attackchain',
            old_name='fairFight',
            new_name='fair_fight',
        ),
        migrations.RenameField(
            model_name='attackchain',
            old_name='groupAttack',
            new_name='group_attack',
        ),
        migrations.RenameField(
            model_name='attackreport',
            old_name='chainBonus',
            new_name='chain_bonus',
        ),
        migrations.RenameField(
            model_name='attackreport',
            old_name='fairFight',
            new_name='fair_fight',
        ),
        migrations.RenameField(
            model_name='attackreport',
            old_name='groupAttack',
            new_name='group_attack',
        ),
        migrations.RenameField(
            model_name='count',
            old_name='fairFight',
            new_name='fair_fight',
        ),
        migrations.RenameField(
            model_name='count',
            old_name='groupAttack',
            new_name='group_attack',
        ),
    ]
