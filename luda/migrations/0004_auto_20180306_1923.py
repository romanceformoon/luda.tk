# Generated by Django 2.0.2 on 2018-03-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luda', '0003_auto_20180306_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='file',
            field=models.ImageField(null=True, upload_to='upload/%Y/%m/%d/'),
        ),
    ]
