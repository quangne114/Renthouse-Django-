# Generated by Django 4.2.5 on 2023-11-26 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0021_alter_room_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 17, 9, 32, 742756, tzinfo=datetime.timezone.utc)),
        ),
    ]
