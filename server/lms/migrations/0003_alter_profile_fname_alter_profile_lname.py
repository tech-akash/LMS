# Generated by Django 4.0.5 on 2022-06-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_alter_profile_courses_enrolled_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Fname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Lname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
