# Generated by Django 4.2.5 on 2023-09-13 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stadiums', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stadium',
            old_name='status',
            new_name='_status',
        ),
    ]
