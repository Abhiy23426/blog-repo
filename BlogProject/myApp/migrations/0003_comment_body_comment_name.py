# Generated by Django 4.1.1 on 2022-10-20 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
