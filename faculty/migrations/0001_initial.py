# Generated by Django 2.2.6 on 2020-03-13 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0015_auto_20200313_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('syllabus', models.FileField(blank=True, null=True, upload_to='syllabi')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2020)),
                ('number', models.IntegerField(choices=[(1, 'First'), (2, 'Second')])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Semester',
                'verbose_name_plural': 'Semesters',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(verbose_name='Date of birth')),
                ('phone_mobile_1', models.CharField(blank=True, max_length=15)),
                ('phone_mobile_2', models.CharField(blank=True, max_length=15)),
                ('phone_home', models.CharField(blank=True, max_length=15)),
                ('address_home', models.TextField(max_length=500)),
                ('address_other', models.TextField(blank=True, max_length=500)),
                ('position', models.CharField(max_length=100)),
                ('hire_date', models.DateField(blank=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=8)),
                ('pay_method', models.CharField(choices=[('Bank', 'Bank'), ('Check', 'Check'), ('Cash', 'Cash')], default='Bank', max_length=50)),
                ('bank', models.CharField(blank=True, choices=[('BAC', 'BAC'), ('BDF', 'BDF'), ('BANPRO', 'BANPRO'), ('LAFISE', 'LAFISE'), ('FICOHSA', 'FICOHSA'), ('BANCORP', 'BANCORP')], max_length=20)),
                ('account', models.CharField(blank=True, max_length=50)),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='faculty.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='CourseStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Student')),
            ],
            options={
                'verbose_name': 'Enrollment',
                'verbose_name_plural': 'Enrollments',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='faculty.Semester'),
        ),
        migrations.AddField(
            model_name='course',
            name='ta_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_ta', to='faculty.Staff'),
        ),
        migrations.AddField(
            model_name='course',
            name='ta_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_ta', to='faculty.Staff'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher', to='faculty.Staff'),
        ),
    ]
