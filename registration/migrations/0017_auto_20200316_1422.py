# Generated by Django 2.2.6 on 2020-03-16 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0016_auto_20200316_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardian',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2),
        ),
    ]
