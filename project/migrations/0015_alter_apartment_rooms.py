# Generated by Django 5.0.7 on 2024-07-20 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_remove_apartment_rooms_apartment_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='rooms',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='project.room'),
        ),
    ]
