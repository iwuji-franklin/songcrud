# Generated by Django 4.1.2 on 2022-11-04 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiste',
            name='last_name',
            field=models.CharField(max_length=1000, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='lyrics',
            name='content',
            field=models.TextField(max_length=50, verbose_name='Content'),
        ),
    ]
