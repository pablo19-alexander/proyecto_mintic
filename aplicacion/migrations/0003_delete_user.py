# Generated by Django 3.2.8 on 2022-09-20 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]