# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subscripcion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('comprador', models.ManyToManyField(to='subscripcion.Persona')),
            ],
        ),
    ]
