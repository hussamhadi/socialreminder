# Generated by Django 4.0.2 on 2022-02-06 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialreminder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='message', to='socialreminder.Tag'),
        ),
    ]
