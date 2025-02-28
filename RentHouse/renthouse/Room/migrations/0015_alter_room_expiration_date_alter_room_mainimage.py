# Generated by Django 4.2.5 on 2023-11-24 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0014_alter_room_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 12, 5, 22, 957150, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='room',
            name='mainimage',
            field=models.ImageField(null=True, upload_to='photo/mainimage'),
        ),
    ]
