# Generated by Django 2.2 on 2019-04-23 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='lat',
            field=models.DecimalField(decimal_places=4, max_digits=7),
        ),
        migrations.AlterField(
            model_name='marker',
            name='lng',
            field=models.DecimalField(decimal_places=4, max_digits=7),
        ),
    ]