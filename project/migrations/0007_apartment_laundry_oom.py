# Generated by Django 5.0.7 on 2024-07-20 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_remove_apartment_kitchen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='laundry_oom',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
