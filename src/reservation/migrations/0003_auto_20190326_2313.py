# Generated by Django 2.1.7 on 2019-03-26 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_vehicule_concessionnaire'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicule',
            old_name='Reservasion',
            new_name='Reservation',
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='Concessionnaire',
            field=models.CharField(default='', max_length=50),
        ),
    ]
