# Generated by Django 3.1.5 on 2021-01-11 16:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='publish_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 11, 16, 9, 34, 500075, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 11, 16, 9, 34, 499474, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='publishion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
