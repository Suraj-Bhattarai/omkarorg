# Generated by Django 3.1.4 on 2021-01-12 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210112_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='warrenty_period',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='warrenty_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
