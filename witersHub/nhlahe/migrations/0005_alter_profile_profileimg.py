# Generated by Django 5.0.1 on 2024-02-08 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhlahe', '0004_followerscount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='blank profile photo.jpeg', upload_to='profile_images'),
        ),
    ]
