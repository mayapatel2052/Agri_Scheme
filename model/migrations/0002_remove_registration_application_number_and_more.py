# Generated by Django 4.0.6 on 2022-08-29 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='Application_Number',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='Confirm_Password',
        ),
    ]
