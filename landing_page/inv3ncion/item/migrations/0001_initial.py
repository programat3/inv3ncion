# Generated by Django 5.0 on 2023-12-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_interno', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
