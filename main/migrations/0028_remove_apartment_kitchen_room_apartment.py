# Generated by Django 5.0.7 on 2024-07-21 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_apartment_kitchen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='kitchen',
        ),
        migrations.AddField(
            model_name='room',
            name='apartment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.apartment'),
            preserve_default=False,
        ),
    ]
