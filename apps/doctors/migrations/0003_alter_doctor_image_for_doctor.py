# Generated by Django 5.0.7 on 2024-07-22 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image_for_doctor',
            field=models.ImageField(upload_to='doctor_images/'),
        ),
    ]
