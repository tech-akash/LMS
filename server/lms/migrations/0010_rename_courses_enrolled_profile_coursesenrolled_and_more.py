# Generated by Django 4.0.5 on 2022-06-29 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0009_course_code_course_unique_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='courses_enrolled',
            new_name='coursesEnrolled',
        ),
        migrations.AddField(
            model_name='result',
            name='startTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('totalMarks', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('timeLimit', models.DateTimeField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.course')),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.quiz'),
        ),
        migrations.AlterField(
            model_name='result',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.quiz'),
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
    ]
