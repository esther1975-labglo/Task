# Generated by Django 4.1.2 on 2022-11-27 06:43

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_remove_restaurant_twitter_handle'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(max_length=100, null=True),
        ),
    ]