# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='location',
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='pk_heigth',
            field=models.IntegerField(),
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='pk_type',
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='pk_weigth',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='pk_type',
            field=models.ManyToManyField(related_name='pkmns', to='pokedex_app.Type'),
        ),
    ]
