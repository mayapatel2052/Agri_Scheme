# Generated by Django 4.0.5 on 2022-09-12 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0007_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schemes',
            name='Schemes_desc',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='Id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]