# Generated by Django 4.1 on 2023-03-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_profile_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.CharField(default='AlphaCode Technology', max_length=255),
        ),
    ]
