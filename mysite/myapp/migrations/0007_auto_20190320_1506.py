# Generated by Django 2.1.7 on 2019-03-20 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20190315_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journeys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journey_score', models.CharField(blank=True, max_length=20)),
                ('date', models.CharField(blank=True, max_length=20)),
                ('start_time', models.CharField(blank=True, max_length=20)),
                ('end_time', models.CharField(blank=True, max_length=20)),
                ('distance', models.CharField(blank=True, max_length=20)),
                ('end_location', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('Driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp.Driver')),
                ('coolent_level', models.CharField(blank=True, max_length=20)),
                ('battery', models.CharField(blank=True, max_length=20)),
                ('oil_level', models.CharField(blank=True, max_length=20)),
                ('windscreen_washer', models.CharField(blank=True, max_length=20)),
                ('break_fluid', models.CharField(blank=True, max_length=20)),
                ('tyre_dept', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20)),
                ('password', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=20)),
                ('phone', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='car',
            old_name='driver',
            new_name='Driver',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='car_milage',
            new_name='car_mileage',
        ),
        migrations.AddField(
            model_name='journeys',
            name='Driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Driver'),
        ),
    ]
