# Generated by Django 2.2.13 on 2021-01-17 09:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('cafeitems', '0003_auto_20020101_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('price', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('image', models.ImageField(default='Not available', upload_to='uploaded_images/')),
                ('date', models.DateTimeField(default=datetime.datetime.today)),
                ('status', models.BooleanField(default=False)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cafeitems.Menu')),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Customer')),
            ],
        ),
    ]