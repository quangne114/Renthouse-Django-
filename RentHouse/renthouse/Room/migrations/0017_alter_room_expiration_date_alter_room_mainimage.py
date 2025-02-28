# Generated by Django 4.2.5 on 2023-11-24 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0016_alter_room_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 14, 17, 41, 55910, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='room',
            name='mainimage',
            field=models.ImageField(blank=True, null=True, upload_to='photo/mainimage'),
        ),
    ]
