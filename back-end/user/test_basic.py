import json
import unittest
from user.views.account import register
from django.test import TestCase, Client
from user.models import EmailPro, Medicine_record, PatientInfo, Sports_record, UserInfo, datum
from user.utils.encrypt import md5
from user.utils.token import create_token, get_username
import datetime

# 为了测试和使用的方便，账号密码邮箱等格式判断在前端进行，因此不包含在单元测试里。这里主要测试向后端输入一些错误数据时能否正确返回。


class MyTestCase(TestCase):

    token = ''
    username = ''
    password = ''
    email = ''
    name = ''
    age = 20
    gender = 1
    disease_type = 1
    birthday = datetime.datetime.now()
    nickname = ''

    @classmethod
    # create account data
    def setUpTestData(self):
        newuser = UserInfo.objects.create(username='sunfy_20020708', password=md5(
            'Sfy_20020708'), email='sunfy20@mails.tsinghua.edu.cn', isActive=True)
        newuser.save()
        newpatient = PatientInfo.objects.create(
            name='test', age=20, gender=1, disease_type=1, userinfo=newuser)
        newpatient.save()
        self.token = create_token('test')
        self.c = Client(HTTP_TOKEN=self.token)

    def test_register(self):
        param = {
            "username": 'sunfy_20020708_2',
            "password": 'Sfy_20020708',
            "email": 'sunfy20@mails.tsinghua.edu.cn',
            "islogin": False,
        }
        response = self.c.post("/login/", data=param,
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_login_success(self):

        param = {
            "username": 'sunfy_20020708',
            "password": 'Sfy_20020708',
            "email": 'sunfy20@mails.tsinghua.edu.cn',
            "islogin": True,
        }
        response = self.c.post("/login/", data=param,
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_login_wrong_password(self):

        param = {
            "username": 'sunfy_20020708',
            "password": 'incorrect',
            "email": 'sunfy20@mails.tsinghua.edu.cn',
            "islogin": True,
        }
        response = self.c.post("/login/", data=param,
                               content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_login_wrong_username(self):

        param = {
            "username": 'sunfy_200',
            "password": 'incorrect',
            "email": 'sunfy20@mails.tsinghua.edu.cn',
            "islogin": True,
        }
        response = self.c.post("/login/", data=param,
                               content_type='application/json')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
