import json

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

import datetime
import threading
from rest_framework import status
from rest_framework.response import Response
from user.models import UserInfo, datum
from user.utils.encrypt import md5


def register(request):
    if request.method == 'POST':
        body = request.body.decode('UTF-8')
        content = json.loads(body)
        username = content['username']
        password = content['password']
        # pwd = md5(password)
        pwd = password
        email = content['email']
        users = UserInfo.objects.filter(username=username)
        if users.exists():
            params = {}
            return HttpResponse(json.dumps(params), status=status.HTTP_401_UNAUTHORIZED)
        newuser = UserInfo(username=username, password=pwd, email=email)
        newuser.save()
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
    print(islogin)
    if islogin == True:
        pwd = password
        # pwd = md5(password)
        users = UserInfo.objects.filter(username=username)
        if users.exists():
            user = users.first()
            # match
            if user.password == pwd:
                params = {}
                # add to session
                request.session['info'] = {'username': user.username}
                # expiry for half an hour
                request.session.set_expiry(60 * 30)
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
            # pwd = password
            email = content['email']
            users = UserInfo.objects.filter(username=username)
            if users.exists():
                params = {}
                return HttpResponse(json.dumps(params), status=status.HTTP_401_UNAUTHORIZED)
            newuser = UserInfo(username=username, password=pwd, email=email)
            newuser.save()
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
