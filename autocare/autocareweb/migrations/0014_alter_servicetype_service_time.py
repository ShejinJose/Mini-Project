# Generated by Django 5.1 on 2024-10-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autocareweb', '0013_servicetype_service_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetype',
            name='service_time',
            field=models.IntegerField(default=60),
        ),
    ]
