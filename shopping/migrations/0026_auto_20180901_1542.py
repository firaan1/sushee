# Generated by Django 2.0.3 on 2018-09-01 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0025_auto_20180901_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placedorder',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('in_progress', 'in_progress'), ('delivered', 'delivered')], default='new', max_length=25),
        ),
    ]