# Generated by Django 5.0.7 on 2024-07-15 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя врача')),
                ('choosing_a_specialization', models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Gynaecologist', 'Gynaecologist'), ('Neurologist', 'Neurologist'), ('Ophthalmologist', 'Ophthalmologist'), ('Paediatrician', 'Paediatrician'), ('General Practitioner', 'General Practitioner')], max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('image_for_doctor', models.ImageField(upload_to='doctors/')),
            ],
        ),
    ]
