# Generated by Django 2.2.7 on 2020-01-09 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_activity_class_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='activityanswer',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
