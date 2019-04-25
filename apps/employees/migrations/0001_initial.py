# Generated by Django 2.0.3 on 2018-03-27 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('masters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Last Updated Date')),
                ('type', models.CharField(choices=[('saving', 'Saving'), ('current', 'Current')], default='saving', max_length=25, verbose_name='Account Type')),
                ('routing_number', models.CharField(blank=True, max_length=100, verbose_name='Routing Number')),
                ('account_number', models.CharField(blank=True, max_length=100, verbose_name='Account Number')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Name')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Address')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name_plural': 'Employee Bank Information',
                'db_table': 'pms_employee_banks',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Last Updated Date')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/employees', verbose_name='Profile Image')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender')], default='male', max_length=25, verbose_name='Employee Gender')),
                ('ssn', models.CharField(blank=True, max_length=50, verbose_name='Employee SSN')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Employee Date of Birth')),
                ('address_1', models.CharField(max_length=255, verbose_name='Address 1')),
                ('address_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address 2')),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Zip Code')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Employee Phone Number')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('blocked', 'Blocked')], default='pending', max_length=25, verbose_name='Employee Status')),
                ('availability', models.CharField(choices=[('available', 'Available'), ('not_available', 'Not Available'), ('hired', 'Hired')], default='available', max_length=20, verbose_name='Employee Status')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='masters.City')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='masters.Country')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='masters.State')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Employees',
                'db_table': 'pms_users_employee_profile',
            },
        ),
        migrations.CreateModel(
            name='EmploymentCompensation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Last Updated Date')),
                ('company', models.CharField(blank=True, max_length=250, null=True, verbose_name='Company')),
                ('location', models.CharField(blank=True, max_length=250, null=True, verbose_name='Location')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Title')),
                ('start_date', models.DateField(null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(null=True, verbose_name='End Date')),
                ('department', models.CharField(blank=True, max_length=100, null=True, verbose_name='Department')),
                ('compensation_type', models.CharField(choices=[('salaried', 'Salaried'), ('daily_payout', 'Daily Payout'), ('fixed_payout', 'Fixed payout')], default='salaried', max_length=25, verbose_name='Compensation Type')),
                ('employment_type', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract')], default='full_time', max_length=25, verbose_name='Employment Type')),
                ('annual_salary', models.IntegerField(default=0, verbose_name='Annual Salary')),
                ('job_duties', models.CharField(blank=True, max_length=250, verbose_name='Performs Exempt Job Duties')),
                ('flsa_classification', models.CharField(blank=True, max_length=250, verbose_name='FLSA Classification')),
                ('manager', models.CharField(blank=True, max_length=250, verbose_name='Manager')),
                ('direct_reports', models.CharField(blank=True, max_length=250, verbose_name='Direct Reports')),
                ('is_currrent', models.BooleanField(default=False, verbose_name='Is Current?')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pms_employee_employments_compensations', to='employees.Employee')),
            ],
            options={
                'verbose_name_plural': 'Employee Employments And Compensations',
                'db_table': 'pms_employee_employments_compensations',
            },
        ),
        migrations.CreateModel(
            name='Paycheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Last Updated Date')),
                ('method', models.CharField(choices=[('bank', 'Bank'), ('paypal', 'Paypal')], default='bank', max_length=25, verbose_name='Method')),
                ('distribution', models.CharField(blank=True, max_length=250, verbose_name='Distribution')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name_plural': 'Employee Paychecks',
                'db_table': 'pms_employee_paycheck',
            },
        ),
    ]
