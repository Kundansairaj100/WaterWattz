# Generated by Django 4.2.5 on 2023-09-19 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('municipal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipalprofile',
            name='is_municipal_user',
            field=models.BooleanField(default=True),
        ),
    ]