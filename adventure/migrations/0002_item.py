# Generated by Django 2.1.1 on 2018-11-07 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='DEFAULT TITLE', max_length=50)),
                ('description', models.CharField(default='DEFAULT DESCRIPTION', max_length=500)),
                ('player', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='adventure.Player')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.Room')),
            ],
        ),
    ]
