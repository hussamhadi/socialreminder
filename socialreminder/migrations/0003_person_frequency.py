# Generated by Django 4.0.2 on 2022-02-06 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialreminder', '0002_message_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='frequency',
            field=models.CharField(blank=True, choices=[('daily', 'daily'), ('weekly mo', 'Weekly on Monday'), ('weekly tu', 'Weekly on Tuesday'), ('weekly we', 'Weekly on Wednesday'), ('weekly thu', 'Weekly on Thursday'), ('weekly fr', 'Weekly on Friday'), ('weekly sa', 'Weekly on Saturday'), ('weekly su', 'Weekly on Sunday'), ('monthly', 'Monthly')], max_length=30, null=True),
        ),
    ]
