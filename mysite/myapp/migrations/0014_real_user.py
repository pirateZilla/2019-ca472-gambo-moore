# Generated by Django 2.1.7 on 2019-04-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_month_journey'),
    ]

    operations = [
        migrations.CreateModel(
            name='real_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(blank=True, max_length=20)),
                ('lat', models.CharField(blank=True, max_length=20)),
                ('lon', models.CharField(blank=True, max_length=20)),
                ('elevation', models.CharField(blank=True, max_length=20)),
                ('accuracy', models.CharField(blank=True, max_length=20)),
                ('bearing', models.CharField(blank=True, max_length=20)),
                ('speed', models.CharField(blank=True, max_length=20)),
                ('satellites', models.CharField(blank=True, max_length=20)),
                ('provider', models.CharField(blank=True, max_length=20)),
                ('hdop', models.CharField(blank=True, max_length=20)),
                ('vdop', models.CharField(blank=True, max_length=20)),
                ('pdop', models.CharField(blank=True, max_length=20)),
                ('geoidheight', models.CharField(blank=True, max_length=20)),
                ('ageofdgpsdata', models.CharField(blank=True, max_length=20)),
                ('dgpsid', models.CharField(blank=True, max_length=20)),
                ('activity', models.CharField(blank=True, max_length=20)),
                ('battery', models.CharField(blank=True, max_length=20)),
                ('annotation', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]