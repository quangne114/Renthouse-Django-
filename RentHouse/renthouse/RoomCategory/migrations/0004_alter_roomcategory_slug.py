# Generated by Django 4.2.5 on 2023-11-09 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoomCategory', '0003_alter_roomcategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomcategory',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
