# Generated by Django 4.2.5 on 2023-11-26 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0017_alter_room_expiration_date_alter_room_mainimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 11, 40, 12, 886314, tzinfo=datetime.timezone.utc)),
        ),
    ]
