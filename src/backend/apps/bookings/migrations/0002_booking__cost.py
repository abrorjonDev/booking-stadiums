# Generated by Django 4.2.5 on 2023-09-13 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='_cost',
            field=models.PositiveBigIntegerField(default=0, verbose_name='cost'),
        ),
    ]
