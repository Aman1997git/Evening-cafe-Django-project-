# Generated by Django 2.2.13 on 2021-01-11 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeitems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.IntegerField(default=0.0),
        ),
    ]
