# Generated by Django 4.0.5 on 2022-12-06 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0015_alter_applied_schemes_farmer_bank_ifsc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemes',
            name='Schemes_desc',
            field=models.CharField(max_length=1000),
        ),
    ]
