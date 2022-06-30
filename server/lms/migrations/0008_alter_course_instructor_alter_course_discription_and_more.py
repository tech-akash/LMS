# Generated by Django 4.0.5 on 2022-06-28 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms', '0007_rename_total_marks_course_totalmarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='discription',
            field=models.TextField(default='abc'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(default='abc', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='progress',
            name='completionPercentage',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='progress',
            name='currMarks',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]