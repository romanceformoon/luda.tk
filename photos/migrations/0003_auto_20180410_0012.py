# Generated by Django 2.0.2 on 2018-04-09 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20161122_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='%Y-%m-%d/'),
        ),
    ]
