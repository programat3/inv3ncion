# Generated by Django 5.0 on 2023-12-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='price',
            field=models.IntegerField(),
        ),
    ]
