# Generated by Django 2.2.6 on 2020-03-16 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['last_name_1', 'last_name_2', 'first_name', 'middle_name']},
        ),
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='staff',
            name='first_name',
            field=models.CharField(default='Paul', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='last_name_1',
            field=models.CharField(default='Manson', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='last_name_2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='notes',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]