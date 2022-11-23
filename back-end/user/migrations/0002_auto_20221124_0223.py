# Generated by Django 3.2.5 on 2022-11-23 18:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'ordering': ['-create_date']},
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='disease_type',
            field=models.SmallIntegerField(choices=[(1, '一型糖尿病'), (2, '二型糖尿病')], default=1, verbose_name='糖尿病类型'),
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='userinfo',
            field=models.OneToOneField(default=23, on_delete=django.db.models.deletion.CASCADE, to='user.userinfo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='注册日期'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别'),
        ),
        migrations.CreateModel(
            name='sports_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='日期')),
                ('sport_type', models.CharField(max_length=64, null=True, verbose_name='运动类型')),
                ('notes', models.CharField(max_length=64, null=True, verbose_name='备注')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_sports_record', to='user.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='datum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_glucose', models.FloatField(null=True, verbose_name='血糖值')),
                ('weight', models.FloatField(null=True, verbose_name='体重')),
                ('blood_pressure', models.FloatField(null=True, verbose_name='血压')),
                ('ketone', models.FloatField(null=True, verbose_name='血酮')),
                ('time_tag', models.SmallIntegerField(choices=[(1, '空腹'), (2, '早餐后'), (3, '午餐前'), (4, '午餐后'), (5, '晚餐前'), (6, '晚餐后')], default=1, verbose_name='录入时段')),
                ('notes', models.CharField(max_length=64, null=True, verbose_name='备注')),
                ('date', models.DateField(auto_now_add=True, verbose_name='日期')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_date', to='user.userinfo')),
            ],
        ),
    ]
