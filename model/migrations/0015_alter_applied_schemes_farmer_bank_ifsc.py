# Generated by Django 4.0.5 on 2022-10-21 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0014_rename_scheme_id_applied_schemes_sch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applied_schemes',
            name='Farmer_Bank_IFSC',
            field=models.CharField(max_length=11),
        ),
    ]
