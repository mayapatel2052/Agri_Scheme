# Generated by Django 4.0.5 on 2022-12-06 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0016_alter_schemes_schemes_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applied_schemes',
            name='Farmer_Account_num',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='applied_schemes',
            name='Schemes_status',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='schemes',
            name='Eligibility',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='schemes',
            name='Ending_date',
            field=models.DateField(max_length=20),
        ),
        migrations.AlterField(
            model_name='schemes',
            name='For_district',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='schemes',
            name='For_taluka',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='schemes',
            name='Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='schemes',
            name='Starting_date',
            field=models.DateField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='District',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='Password',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='user',
            name='Taluka',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='Village',
            field=models.CharField(max_length=30),
        ),
    ]