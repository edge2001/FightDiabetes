# Generated by Django 4.0.4 on 2022-12-20 07:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20221220_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine_record',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 15, 37, 18, 702926), verbose_name='日期时间'),
        ),
        migrations.AlterField(
            model_name='sports_record',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 15, 37, 18, 702540), verbose_name='日期时间'),
        ),
    ]
