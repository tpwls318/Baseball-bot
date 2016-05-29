# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-29 04:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hitter',
            fields=[
                ('player_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hello.Player')),
                ('hit_hand', models.CharField(max_length=50)),
                ('avg', models.DecimalField(decimal_places=3, max_digits=4)),
                ('obp', models.DecimalField(decimal_places=3, max_digits=4)),
                ('hr', models.PositiveSmallIntegerField()),
                ('rbi', models.PositiveSmallIntegerField()),
                ('r', models.PositiveSmallIntegerField()),
            ],
            bases=('hello.player',),
        ),
        migrations.CreateModel(
            name='Pitcher',
            fields=[
                ('player_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hello.Player')),
                ('pit_hand', models.CharField(max_length=50)),
                ('kinds', models.CharField(max_length=50)),
                ('era', models.DecimalField(decimal_places=2, max_digits=4)),
                ('w', models.PositiveSmallIntegerField()),
                ('l', models.PositiveSmallIntegerField()),
                ('sv', models.PositiveSmallIntegerField()),
                ('k9', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            bases=('hello.player',),
        ),
    ]
