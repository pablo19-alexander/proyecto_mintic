# Generated by Django 3.2.8 on 2022-10-05 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0011_auto_20221004_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultado_cliente',
            name='requerimiento',
        ),
        migrations.AddField(
            model_name='resultado_cliente',
            name='requerimiento',
            field=models.ManyToManyField(blank=True, null=True, to='aplicacion.Item'),
        ),
    ]