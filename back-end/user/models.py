from django.db import models

# Create your models here.


class UserInfo(models.Model):
    create_date = models.DateTimeField(auto_now_add=True,verbose_name='注册日期')
    id = models.AutoField(verbose_name='id', primary_key= True)
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.CharField(verbose_name='Email', max_length = 64)
    
    class Meta:
        ordering = ('create_date',)


class PatientInfo(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=16)
    age = models.IntegerField(verbose_name='年龄')
    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)
    disease_types = (
        (1,'一型糖尿病'),
        (2,'二型糖尿病')
    )
    disease_type = models.SmallIntegerField(verbose_name='糖尿病类型', choices=disease_types)
    userinfo = models.OneToOneField(UserInfo,on_delete=models.CASCADE)

class datum(models.Model):
    blood_glucose = models.FloatField(verbose_name='血糖值',null=True)
    weight = models.FloatField(verbose_name='体重',null=True)
    blood_pressure = models.FloatField(verbose_name='血压',null=True)
    ketone = models.FloatField(verbose_name='血酮',null=True)
    time_tags = (
        (1, '空腹'),
        (2, '早餐后'),
        (3, '午餐前'),
        (4, '午餐后'),
        (5, '晚餐前'),
        (6, '晚餐后'),
    )
    time_tag = models.SmallIntegerField(verbose_name='录入时段', choices=time_tags)
    notes = models.CharField(verbose_name='备注',null=True,max_length=64)
    date = models.DateField(verbose_name='日期',auto_now_add=True)
    user = models.ForeignKey(UserInfo,related_name='user_date',on_delete=models.CASCADE)


class sports_record(models.Model):
    date = models.DateField(verbose_name='日期',auto_now_add=True)
    sport_type = models.CharField(verbose_name='运动类型', null=True,max_length=64)
    notes = models.CharField(verbose_name='备注',null=True,max_length=64)
    user = models.ForeignKey(UserInfo,related_name='user_sports_record',on_delete=models.CASCADE)




    
    




