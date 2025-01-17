# Generated by Django 5.1 on 2024-10-20 15:51

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autocareweb', '0014_alter_servicetype_service_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=20, unique=True)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('confirmed', 'Confirmed')], default='pending', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autocareweb.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='OrderService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='autocareweb.order')),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autocareweb.servicetype')),
            ],
        ),
    ]
