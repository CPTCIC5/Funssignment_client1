# Generated by Django 3.2 on 2021-11-25 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male')], max_length=20),
        ),
    ]
