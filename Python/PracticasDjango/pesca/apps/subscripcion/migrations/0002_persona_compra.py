# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_remove_inventario_comprador'),
        ('subscripcion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='compra',
            field=models.ManyToManyField(blank=True, to='inventario.Inventario'),
        ),
    ]
