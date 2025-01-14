# Generated by Django 2.1.7 on 2019-03-17 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('version', '0001_initial'),
        ('option', '0006_auto_20190317_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option_Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Default', models.BooleanField(default=False)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='option.Option')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='version.Version')),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='Option_Version',
            field=models.ManyToManyField(through='option.Option_Version', to='version.Version'),
        ),
    ]
