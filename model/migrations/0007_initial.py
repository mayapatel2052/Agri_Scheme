# Generated by Django 4.0.5 on 2022-09-08 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('model', '0006_delete_reg_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='schemes',
            fields=[
                ('Schemes_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Eligibility', models.CharField(max_length=20)),
                ('For_district', models.CharField(max_length=20)),
                ('For_taluka', models.CharField(max_length=20)),
                ('Starting_date', models.DateField(max_length=10)),
                ('Ending_date', models.DateField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('Id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Mobile_number', models.CharField(max_length=10)),
                ('Name', models.CharField(max_length=50)),
                ('User_type', models.CharField(max_length=20)),
                ('Valid_user_or_not', models.BooleanField()),
                ('Servay_num', models.CharField(max_length=10)),
                ('Password', models.CharField(max_length=8)),
                ('District', models.CharField(max_length=20)),
                ('Taluka', models.CharField(max_length=20)),
                ('Village', models.CharField(max_length=20)),
                ('Land_area', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Schemes_Status',
            fields=[
                ('Id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Farmer_Mobile', models.CharField(max_length=10)),
                ('Farmer_name', models.CharField(max_length=50)),
                ('Schemes_status', models.CharField(max_length=20)),
                ('Scheme_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.schemes')),
            ],
        ),
    ]
