# Generated by Django 4.2 on 2023-10-19 23:23

import datetime
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
            name='Jop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jop_title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='', verbose_name='photos/%y%m%d')),
                ('company_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 10, 19, 23, 23, 24, 999728, tzinfo=datetime.timezone.utc))),
                ('jop_nature', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Remote', 'Remote'), ('Freelance', 'Freelance')], max_length=20)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
