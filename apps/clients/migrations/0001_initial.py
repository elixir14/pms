# Generated by Django 2.0.3 on 2018-03-27 12:26

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
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Last Updated Date')),
                ('name', models.CharField(max_length=100, verbose_name='Client Name')),
                ('trade', models.CharField(max_length=100, verbose_name='Trade')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email Address')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('contact_first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='First Name')),
                ('contact_last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Last Name')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Phone Number')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('blocked', 'Blocked')], default='pending', max_length=25, verbose_name='Employee Status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Clients',
                'db_table': 'pms_clients_client',
            },
        ),
    ]