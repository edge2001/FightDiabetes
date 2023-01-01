# Generated by Django 3.2.5 on 2022-12-11 03:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20221203_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datum',
            name='date',
            field=models.DateField(verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='datum',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='user_data',
                to='user.userinfo'),
        ),
    ]
