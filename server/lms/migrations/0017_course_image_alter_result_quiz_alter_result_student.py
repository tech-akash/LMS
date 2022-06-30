# Generated by Django 4.0.5 on 2022-06-29 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms', '0016_result_unique_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='./image'),
        ),
        migrations.AlterField(
            model_name='result',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.quiz'),
        ),
        migrations.AlterField(
            model_name='result',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
