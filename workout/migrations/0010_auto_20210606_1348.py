# Generated by Django 3.2.3 on 2021-06-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0009_auto_20210606_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutplan',
            name='break_days_between_sessions',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workoutplan',
            name='workout_session_row',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
