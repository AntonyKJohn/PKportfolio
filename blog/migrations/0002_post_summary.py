# Generated by Django 3.0.7 on 2020-06-09 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.TextField(default='null'),
        ),
    ]
