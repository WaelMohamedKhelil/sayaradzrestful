# Generated by Django 2.1.7 on 2019-03-12 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modele', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modele',
            name='Image',
            field=models.ImageField(blank=True, default='modele/default.png', upload_to='modele'),
        ),
    ]