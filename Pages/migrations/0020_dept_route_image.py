# Generated by Django 2.2.8 on 2020-02-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0019_hospital_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='dept',
            name='route_image',
            field=models.ImageField(default='', upload_to='Department_route'),
        ),
    ]
