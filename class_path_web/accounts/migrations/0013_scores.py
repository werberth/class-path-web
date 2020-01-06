# Generated by Django 2.2.7 on 2020-01-06 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20191230_0230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_score', models.FloatField(null=True, verbose_name='first score')),
                ('second_score', models.FloatField(null=True, verbose_name='second score')),
                ('third_score', models.FloatField(null=True, verbose_name='third score')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='accounts.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='accounts.Student')),
            ],
            options={
                'db_table': 'scores',
            },
        ),
    ]
