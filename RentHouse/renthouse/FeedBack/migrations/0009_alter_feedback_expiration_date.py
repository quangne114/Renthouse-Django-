# Generated by Django 4.2.5 on 2023-11-27 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeedBack', '0008_alter_feedback_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 11, 14, 6, 13, 849032, tzinfo=datetime.timezone.utc)),
        ),
    ]
