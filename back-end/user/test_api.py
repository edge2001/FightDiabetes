import json
import unittest
from user.views.account import register
from django.test import TestCase, Client
from user.models import EmailPro, Medicine_record, PatientInfo, Sports_record, UserInfo, datum
from user.utils.encrypt import md5
from user.utils.token import create_token, get_username
import datetime
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vue-admin-webapp.settings')
django.setup()


class MyTestCase(TestCase):

    token = ''
    username = 'test'
    password = 'szx'
    email = 'song_zixuan@sina.cn'
    name = 'test'
    age = 20
    gender = 1
    disease_type = 1
    birthday = datetime.datetime.now()
    nickname = 'Alice'

    @classmethod
    # create account data
    def setUpTestData(self):
        newuser = UserInfo.objects.create(username='test', password=md5(
            'szx'), email='song_zixuan@sina.cn', isActive=True)
        newuser.save()
        newpatient = PatientInfo.objects.create(
            name='test', age=20, gender=1, disease_type=1, userinfo=newuser)
        newpatient.save()
        self.token = create_token('test')
        self.c = Client(HTTP_TOKEN=self.token)

    # login

    def test_login(self):

        param = {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "islogin": True,
        }
        response = self.c.post("/login/", data=param,
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # save info
    def test_saveinfo(self):
        param = {
            'email': self.email,
            'birth': self.birthday,
            'gender': self.gender,
            'disease_type': self.disease_type,
            'name': self.name,
            'nickname': self.nickname
        }
        response = self.c.post("/saveinfo/", data=param,
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # check info
    def test_checkinfo(self):
        response = self.c.get("/saveinfo/", content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # add sports record
    def test_addsportsrecord(self):
        param = {
            'sport_type': 'basketball',
            'datetime': datetime.datetime.now(),
            'notes': 'test',
        }
        response = self.c.post("/add_sports_record/",
                               data=param, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # get sports data
    def test_getsportsdata(self):
        response = self.c.get("/get_sports_data/",
                              content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # add medicine record
    def test_addmedicinerecord(self):
        param = {
            'medicine_type': '胰岛素',
            'datetime': datetime.datetime.now(),
            'notes': 'test',
            'quantity': 1,
        }
        response = self.c.post("/add_medicine_record/",
                               data=param, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # get medicine data
    def test_getmedicinedata(self):
        response = self.c.get("/get_medicine_data/",
                              content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # get medicine time
    def test_getmedicinetime(self):
        response = self.c.get("/getMedicineTime/",
                              content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # check database
    def test_checkdatabase(self):
        response = self.c.get("/show/", content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # add datum
    def test_adddatum(self):
        param = {
            'blood_glucose': '1',
            'weight': 88,
            'ketone': 2,
            'pressure': 22,
            'time_tag': 2,
            'notes': 'test',
        }
        response = self.c.post("/add_datum/", data=param,
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # get week glucose
    def test_getweekglucose(self):
        param = {
            'time_tag': 1,
        }
        response = self.c.post("/get_week_glucose/",
                               data=param, content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
