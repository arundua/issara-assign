# Generated by Django 5.1 on 2024-08-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarDealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_en', models.CharField(blank=True, max_length=255, null=True)),
                ('license_number', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('logo', models.URLField(blank=True, max_length=500, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('rating_score', models.FloatField()),
                ('rating_count', models.IntegerField()),
                ('comments_count', models.IntegerField()),
                ('popularity', models.IntegerField()),
                ('city', models.IntegerField()),
            ],
        ),
    ]
