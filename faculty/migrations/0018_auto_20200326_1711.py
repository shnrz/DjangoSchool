# Generated by Django 2.2.6 on 2020-03-26 23:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0017_auto_20200326_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='hire_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]