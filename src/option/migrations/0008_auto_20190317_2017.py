# Generated by Django 2.1.7 on 2019-03-17 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0007_auto_20190317_1908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='Option_Version',
            new_name='option_Version',
        ),
    ]
