# Generated by Django 2.0.3 on 2018-08-30 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0012_auto_20180830_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='kurtarate',
            name='dresstype',
            field=models.CharField(default='kurta', editable=False, max_length=25),
        ),
        migrations.AddField(
            model_name='sareerate',
            name='dresstype',
            field=models.CharField(default='saree', editable=False, max_length=25),
        ),
        migrations.AddField(
            model_name='toprate',
            name='dresstype',
            field=models.CharField(default='top', editable=False, max_length=25),
        ),
        migrations.AddField(
            model_name='trouserrate',
            name='dresstype',
            field=models.CharField(default='trouser', editable=False, max_length=25),
        ),
    ]
