# Generated by Django 2.2.7 on 2020-01-09 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_auto_20191214_0905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
