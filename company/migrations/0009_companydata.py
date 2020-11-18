# Generated by Django 3.1.2 on 2020-11-18 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_auto_20201117_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ts', models.IntegerField(default=0)),
                ('timestamp', models.IntegerField(default=0)),
                ('employees_hired', models.IntegerField(default=0)),
                ('popularity', models.IntegerField(default=0)),
                ('efficiency', models.IntegerField(default=0)),
                ('environment', models.IntegerField(default=0)),
                ('daily_income', models.BigIntegerField(default=0)),
                ('daily_customers', models.IntegerField(default=0)),
                ('weekly_income', models.BigIntegerField(default=0)),
                ('weekly_customers', models.IntegerField(default=0)),
                ('advertising_budget', models.IntegerField(default=0)),
                ('employees', models.TextField(default='{}')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]
