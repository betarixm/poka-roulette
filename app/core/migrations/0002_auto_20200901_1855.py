# Generated by Django 3.1 on 2020-09-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roulette', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='items',
        ),
        migrations.AddField(
            model_name='user',
            name='rounds',
            field=models.ManyToManyField(to='roulette.Round', verbose_name='참여한 라운드'),
        ),
    ]