import json

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.middleware.csrf import get_token
import datetime
import threading

from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.response import Response
from user.models import UserInfo, datum, EmailPro
from user.utils.encrypt import md5
from user.utils.token import get_username
from random import Random

from django.core.mail import send_mail
from server.settings import EMAIL_FROM
from django.views import View
from user.utils.token import create_token
# 随机生成字符串


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str   # 将拼接的字符串返回


def register(request):
    if request.method == 'POST':
        body = request.body.decode('UTF-8')
        content = json.loads(body)
        username = content['username']
        password = content['password']
        pwd = md5(password)
        email = content['email']
        users = UserInfo.objects.filter(username=username)
        if users.exists():
            params = {}
            return HttpResponse(json.dumps(params), status=status.HTTP_401_UNAUTHORIZED)
        newuser = UserInfo(username=username, password=pwd, email=email)
        newuser.save()
        print('要注册了')
        send_register_email(email, 'register')
        params = {
            'username': username,
            'password': pwd,
            'email': email
        }
        return HttpResponse(json.dumps(params), status=status.HTTP_200_OK)
    else:
        params = {'username': '', 'password': ''}
        return HttpResponse(json.dumps(params), status=status.HTTP_401_UNAUTHORIZED)


def login(request):
    body = request.body
    content = json.loads(body)
    username = content['username']
    password = content['password']
    islogin = content['islogin']
    print('login:', islogin)
    if islogin == True:
        pwd = md5(password)
        users = UserInfo.objects.filter(username=username)
        if users.exists():
            user = users.first()
            # match
            if user.password == pwd:
                # add to session
                #request.session['info'] = {'username': user.username}
                # expiry for half an hour
                #request.session.set_expiry(60 * 30)

                token = create_token(username)
                params = {'token': token,
                          'username': username
                          }
                return HttpResponse(json.dumps(params), status=status.HTTP_200_OK)
            # doesn't match
            else:
                params = {}
                return HttpResponse(json.dumps(params), status=status.HTTP_401_UNAUTHORIZED)
        # user doesn't exist
        else:
            params = {}
            return HttpResponse(json.dumps(params), status=status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'POST':
            body = request.body.decode('UTF-8')
            content = json.loads(body)
            username = content['username']
            password = content['password']
            pwd = md5(password)
            email = content['email']
            users = UserInfo.objects.filter(username=username)
            if users.exists():
                params = {}
                return HttpResponse(json.dumps(params), status=status.HTTP_401_UNAUTHORIZED)
            newuser = UserInfo(username=username, password=pwd,
                               email=email, isActive=False)
            newuser.save()
            print('要注册了')
            send_register_email(email, 'register')
            params = {
                'username': username,
                'password': pwd,
                'email': email
            }
            return HttpResponse(json.dumps(params), status=status.HTTP_200_OK)
        else:
            params = {'username': '', 'password': ''}
            return HttpResponse(json.dumps(params), status=status.HTTP_401_UNAUTHORIZED)


def logout(request):
    # clear session data
    request.session.clear()
    return HttpResponse(status=status.HTTP_200_OK)

# just used for checking, delete after deploy


def show_list(request):
    all_users = UserInfo.objects.all()
    params = []
    for user in all_users:
        username = user.username
        # print(username)
        password = user.password
        email = user.email
        param = {
            'username': username,
            'password': password,
            'email': email
        }
        params.append(param)

    return HttpResponse(params, status=status.HTTP_200_OK)


def get_user_info(request, id):
    user = UserInfo.objects.get(id=id)
    username = user.username
    email = user.email
    params = {
        'uname': username,
        'email': email
    }
    return HttpResponse(params, status=status.HTTP_200_OK)

    # 验证邮箱相关


def send_register_email(email, send_type='register'):  # 类型为注册
    email_recode = EmailPro()
    code = random_str(16)  # 生成16位的随机字符串
    email_recode.code = code
    email_recode.email = email
    email_recode.send_type = send_type
    email_recode.save()

    email_title = ''
    email_body = ''
    if send_type == 'register':
        email_title = '注册激活链接'
        email_body = '请点击下方的链接激活你的账号：http://127.0.0.1:8000/active/{0}'.format(
            code)
    else:
        pass  # 忘记密码--暂时不写
    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    if send_status:
        pass
    print('发出邮件')

def save_user_info(request):
    if request.method == 'GET':
        token = request.META.get('HTTP_TOKEN')
        username = get_username(token)

        user = UserInfo.objects.get(username=username)
        params = {
            'name' : user.patientinfo.name,
            'age' : user.patientinfo.age,
            'gender' : user.patientinfo.gender,
            'disease_type' : user.patientinfo.disease_type,
            # 'create_date' : user.create_date,
            'username' : user.username,
            'email' : user.email,
        }
        print(params)
    return HttpResponse(json.dumps(params), status=status.HTTP_200_OK)








class ActiveUserView(View):
    def get(self, request, active_code):
        all_codes = EmailPro.objects.filter(code=active_code)
        if all_codes:
            for recode in all_codes:
                email = recode.email
                user = UserInfo.objects.get(email=email)
                user.isActive = True
                user.save()
                print('激活成功')
            # 转移到登录页面
        else:
            pass
            # 转移到注册页面

