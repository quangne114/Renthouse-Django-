# Generated by Django 4.2.5 on 2023-11-27 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeedBack', '0005_alter_feedback_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 11, 11, 57, 29, 339406, tzinfo=datetime.timezone.utc)),
        ),
    ]
