# Generated by Django 3.2.8 on 2022-10-05 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0013_alter_resultado_cliente_checked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultado_cliente',
            name='requerimiento',
        ),
        migrations.AddField(
            model_name='resultado_cliente',
            name='requerimiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.item'),
        ),
    ]
