# Generated by Django 5.0.4 on 2024-04-18 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_lenovo_image_alter_lenovo_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lenovo',
            name='image',
            field=models.ImageField(upload_to='fooditem'),
        ),
        migrations.AlterField(
            model_name='lenovo',
            name='video',
            field=models.FileField(upload_to='fooditem'),
        ),
    ]
