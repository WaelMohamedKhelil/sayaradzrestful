# Generated by Django 2.1.7 on 2019-03-12 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('Code_Option', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Nom_Option', models.CharField(max_length=100)),
            ],
        ),
    ]
