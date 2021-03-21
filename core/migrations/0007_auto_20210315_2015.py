# Generated by Django 3.0 on 2021-03-15 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_product_best_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cloudName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_tag',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='video_tag',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]