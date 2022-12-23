# Generated by Django 3.2.16 on 2022-12-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='img')),
                ('description', models.TextField()),
                ('active', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_veg', models.BooleanField()),
                ('quantity', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
