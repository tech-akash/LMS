# Generated by Django 4.0.5 on 2022-06-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0013_remove_question_assignment_question_alloptions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='options',
            name='question',
        ),
        migrations.AddField(
            model_name='result',
            name='chooseOptions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ChoosenOption',
        ),
        migrations.DeleteModel(
            name='Options',
        ),
    ]
