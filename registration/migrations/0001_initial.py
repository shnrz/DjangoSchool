# Generated by Django 2.2.6 on 2019-12-12 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name_1', models.CharField(max_length=50)),
                ('last_name_2', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('notes', models.TextField(blank=True, max_length=1000)),
                ('phone_mobile_1', models.CharField(blank=True, max_length=15)),
                ('phone_mobile_2', models.CharField(blank=True, max_length=15)),
                ('phone_home', models.CharField(blank=True, max_length=15)),
                ('phone_work', models.CharField(blank=True, max_length=15)),
                ('address_home', models.TextField(max_length=500)),
                ('address_work', models.TextField(max_length=500)),
                ('address_other', models.TextField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name_1', models.CharField(max_length=50)),
                ('last_name_2', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('notes', models.TextField(blank=True, max_length=1000)),
                ('dob', models.DateField(verbose_name='Date of birth')),
                ('phone_mobile_1', models.CharField(blank=True, max_length=15)),
                ('phone_home', models.CharField(blank=True, max_length=15)),
                ('relation_1', models.CharField(max_length=100)),
                ('relation_2', models.CharField(max_length=100)),
                ('guardian_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='guardian_1', to='registration.Guardian')),
                ('guardian_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guardian_2', to='registration.Guardian')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField(auto_now_add=True)),
                ('grade', models.IntegerField()),
                ('notes', models.TextField(max_length=1000)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Student')),
            ],
        ),
    ]