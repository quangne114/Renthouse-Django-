# Generated by Django 4.2.5 on 2023-12-03 12:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0027_alter_room_price_alter_room_price_deposit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 17, 12, 1, 22, 435707, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='room_images/')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Room.room')),
            ],
        ),
    ]
