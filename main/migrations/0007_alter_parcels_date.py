# Generated by Django 3.2.7 on 2021-09-20 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_parcels_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcels',
            name='date',
            field=models.DateField(default='20.09.2021'),
        ),
    ]
