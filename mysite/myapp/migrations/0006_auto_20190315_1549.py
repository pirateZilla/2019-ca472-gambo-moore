# Generated by Django 2.1.7 on 2019-03-15 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='Driver',
            new_name='driver',
        ),
    ]
