# Generated by Django 5.0.7 on 2024-07-20 22:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0024_remove_room_apartment_room_apartment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='apartment',
        ),
        migrations.AddField(
            model_name='room',
            name='apartment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='apartment', to='project.apartment'),
            preserve_default=False,
        ),
    ]
