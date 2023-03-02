# Generated by Django 2.2.6 on 2020-03-02 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_auto_20191225_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentguardian',
            name='guardian',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_guardian', to='registration.Guardian'),
        ),
        migrations.AlterField(
            model_name='studentguardian',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_guardian', to='registration.Student'),
        ),
    ]