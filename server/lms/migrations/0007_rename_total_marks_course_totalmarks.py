# Generated by Django 4.0.5 on 2022-06-28 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_remove_progress_totalmarks_course_total_marks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='total_marks',
            new_name='totalMarks',
        ),
    ]
