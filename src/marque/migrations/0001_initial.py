# Generated by Django 2.1.7 on 2019-03-10 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('Id_Marque', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Nom_Marque', models.CharField(max_length=100)),
            ],
        ),
    ]