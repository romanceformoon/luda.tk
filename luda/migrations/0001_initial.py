# Generated by Django 2.0.2 on 2018-03-06 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gmy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif_name', models.CharField(default='', max_length=9999)),
            ],
        ),
        migrations.CreateModel(
            name='My',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(default='', max_length=9999)),
            ],
        ),
    ]
