# Generated by Django 2.2.6 on 2019-12-12 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20191212_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardian',
            name='phone_mobile_1',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='phone_mobile_2',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='student',
            name='guardian_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guardian_2', to='registration.Guardian'),
        ),
        migrations.AlterField(
            model_name='student',
            name='relation_2',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
