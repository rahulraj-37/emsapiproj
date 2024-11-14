# Generated by Django 5.1.3 on 2024-11-11 10:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apibackendapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=200)),
                ('Designation', models.CharField(max_length=150)),
                ('Dateofjoining', models.DateField()),
                ('Contact', models.CharField(max_length=150)),
                ('IsActive', models.BooleanField(default=True)),
                ('DepartmentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apibackendapp.department')),
            ],
        ),
    ]
