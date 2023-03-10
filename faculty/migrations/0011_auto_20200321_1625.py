# Generated by Django 2.2.6 on 2020-03-21 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0010_auto_20200321_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='ta_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ta1_course', to='faculty.Staff'),
        ),
        migrations.AlterField(
            model_name='course',
            name='ta_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ta2_course', to='faculty.Staff'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_course', to='faculty.Staff'),
        ),
    ]
