# Generated by Django 5.1 on 2024-10-20 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autocareweb', '0012_alter_mechanic_level_alter_mechanic_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='service_time',
            field=models.TimeField(default='01:00:00'),
        ),
    ]
