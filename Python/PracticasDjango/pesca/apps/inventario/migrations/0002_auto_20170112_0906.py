# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='comprador',
            field=models.ManyToManyField(blank=True, to='subscripcion.Persona'),
        ),
    ]
