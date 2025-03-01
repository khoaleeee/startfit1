# Generated by Django 5.1.5 on 2025-02-22 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activitie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('bodyParts', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrackedActivitie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activityType', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('notes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=12)),
                ('passwd', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
