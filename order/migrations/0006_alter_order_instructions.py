# Generated by Django 4.1.2 on 2022-11-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='instructions',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
