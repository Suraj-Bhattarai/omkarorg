# Generated by Django 3.1.4 on 2021-01-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210112_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='best_seller',
            field=models.BooleanField(default=False),
        ),
    ]
