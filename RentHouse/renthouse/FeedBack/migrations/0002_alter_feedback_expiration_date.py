# Generated by Django 4.2.5 on 2023-11-26 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeedBack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 11, 56, 47, 241721, tzinfo=datetime.timezone.utc)),
        ),
    ]
