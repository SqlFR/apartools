# Generated by Django 5.0.7 on 2024-07-20 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0007_alter_issue_apartment_remove_issue_room_issue_room'),
        ('project', '0022_alter_room_apartment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='room',
        ),
        migrations.AddField(
            model_name='issue',
            name='room',
            field=models.ManyToManyField(related_name='apartments', to='project.room'),
        ),
    ]
