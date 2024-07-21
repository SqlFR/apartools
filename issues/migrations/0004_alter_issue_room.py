# Generated by Django 5.0.7 on 2024-07-20 22:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_alter_issue_options_issue_room'),
        ('main', '0020_remove_apartment_rooms_room_apartment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.room'),
        ),
    ]
