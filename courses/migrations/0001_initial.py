# Generated by Django 4.2.7 on 2023-12-08 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Chapter',
                'verbose_name_plural': 'Chapters',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='static/courses_images/')),
                ('price', models.IntegerField()),
                ('lavel', models.CharField(choices=[('Beginner', 'Beginner'), ('Amateur', 'Amateur'), ('Professional', 'Professional')], max_length=20)),
                ('discount', models.IntegerField(default=0)),
                ('is_purchased', models.BooleanField(default=False)),
                ('is_saved', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('video_path', models.FileField(upload_to='static/course-class_videos/')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.chapter')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
        ),
        migrations.CreateModel(
            name='UserLessonRewiew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_watched', models.DateTimeField(blank=True, null=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vieo_lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
            ],
            options={
                'verbose_name': 'UserRewiew',
                'verbose_name_plural': 'UserRewiews',
            },
        ),
        migrations.CreateModel(
            name='CourceComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('title', models.TextField()),
                ('is_complained', models.BooleanField(default=False)),
                ('cource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
            options={
                'verbose_name': 'CourceComment',
                'verbose_name_plural': 'CourceComments',
            },
        ),
    ]
