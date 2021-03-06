# Generated by Django 2.2.7 on 2019-11-17 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityanswer',
            name='google_drive_file_key',
        ),
        migrations.AddField(
            model_name='activityanswer',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='answers'),
        ),
        migrations.AddField(
            model_name='activityanswer',
            name='type',
            field=models.CharField(choices=[('image', 'Image'), ('audio', 'Audio'), ('video', 'Video')], default='image', max_length=10),
            preserve_default=False,
        ),
    ]
