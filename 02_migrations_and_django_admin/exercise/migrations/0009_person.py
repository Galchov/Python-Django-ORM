# Generated by Django 5.2 on 2025-04-28 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.PositiveIntegerField()),
                ('age_group', models.CharField(default='No age group', max_length=20)),
            ],
        ),
    ]
