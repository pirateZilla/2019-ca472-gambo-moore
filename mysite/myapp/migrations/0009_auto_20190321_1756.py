# Generated by Django 2.1.7 on 2019-03-21 17:56

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20190321_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_mileage',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine_size',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='dob',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='journeys',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='journeys',
            name='distance',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='journeys',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='journeys',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='battery',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='break_fluid',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='coolent_level',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='oil_level',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='tyre_dept',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='windscreen_washer',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
