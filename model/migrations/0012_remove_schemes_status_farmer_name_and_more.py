# Generated by Django 4.0.5 on 2022-10-14 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0011_alter_schemes_status_schemes_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schemes_status',
            name='Farmer_name',
        ),
        migrations.AlterField(
            model_name='schemes_status',
            name='Farmer_Mobile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.user'),
        ),
    ]
