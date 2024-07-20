# Generated by Django 5.0.7 on 2024-07-20 20:21

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_room_number_room_room_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='bathroom',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='bedroom',
        ),
        migrations.AlterField(
            model_name='apartment',
            name='kitchen',
            field=models.ForeignKey(limit_choices_to={'room_type': 'KI'}, on_delete=django.db.models.deletion.CASCADE, related_name='Cuisine', to='main.room'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='laundry_room',
            field=models.ForeignKey(limit_choices_to={'room_type': 'LA'}, on_delete=django.db.models.deletion.CASCADE, related_name='Buanderie', to='main.room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('BE', 'Chambre'), ('BA', 'Salle de bain'), ('KI', 'Cuisine'), ('LI', 'Salon'), ('LA', 'Buanderie'), ('EN', 'Entrée')], max_length=2),
        ),
        migrations.AddField(
            model_name='apartment',
            name='bathroom',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AddField(
            model_name='apartment',
            name='bedroom',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
