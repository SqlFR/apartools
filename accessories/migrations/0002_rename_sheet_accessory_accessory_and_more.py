# Generated by Django 5.0.7 on 2024-08-11 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accessories', '0001_initial'),
        ('project', '0029_rename_number_of_bathrooms_apartment_bathroom_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessory',
            old_name='sheet',
            new_name='accessory',
        ),
        migrations.AlterUniqueTogether(
            name='accessory',
            unique_together={('apartment', 'accessory')},
        ),
    ]
