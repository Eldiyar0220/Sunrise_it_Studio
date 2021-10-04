# Generated by Django 3.2.7 on 2021-09-17 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_category_post_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='parcels',
            name='date',
            field=models.DateField(default='17.09.2021'),
        ),
    ]