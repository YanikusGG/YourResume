# Generated by Django 4.1.4 on 2022-12-07 23:19

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
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('university_name', models.CharField(max_length=100)),
                ('university_specialization', models.CharField(max_length=100)),
                ('university_start_date', models.CharField(max_length=100)),
                ('university_end_date', models.CharField(max_length=100)),
                ('work_name', models.CharField(max_length=100)),
                ('work_specialization', models.CharField(max_length=100)),
                ('work_start_date', models.CharField(max_length=100)),
                ('work_end_date', models.CharField(max_length=100)),
                ('work_projects', models.TextField()),
                ('skills', models.CharField(max_length=100)),
                ('hobbies', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
