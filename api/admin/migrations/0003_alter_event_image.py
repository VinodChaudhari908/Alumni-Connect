# Generated by Django 4.1.6 on 2023-02-06 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Image',
            field=models.ImageField(upload_to=''),
        ),
    ]
