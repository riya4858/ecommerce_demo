# Generated by Django 4.2.6 on 2023-11-10 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
