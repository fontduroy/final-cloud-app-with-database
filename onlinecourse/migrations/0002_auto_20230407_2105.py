# Generated by Django 3.1.3 on 2023-04-07 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='text',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(default='', max_length=1024),
        ),
    ]
