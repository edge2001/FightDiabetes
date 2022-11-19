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

from .models import UserInfo


def register(request):
    if request.method == 'POST':
        body = request.body.decode('UTF-8')
        content = json.loads(body)
        username = content['username']
        password = content['password']
        email = content['email']
        users = UserInfo.objects.filter(username=username)
        if users.exists():
            params = {}
            return HttpResponse(json.dumps(params), status=status.HTTP_401_UNAUTHORIZED)
        newuser = UserInfo(username=username, password=password, email=email)
        newuser.save()
        params = {
            'username': username,
            'password': password,
            'email': email
        }
        return HttpResponse(json.dumps(params), status=status.HTTP_200_OK)

    return HttpResponse(json.dumps(params), status=status.HTTP_401_UNAUTHORIZED)


def login(request):
    body = request.body
    content = json.loads(body)
    username = content['username']
    password = content['password']
    users = UserInfo.objects.filter(username=username)
    if users.exists():
        user = users.first()
        if user.password == password:
            params = {}
            return HttpResponse(json.dumps(params), status=status.HTTP_200_OK)
        else:
            params = {}
            return HttpResponse(json.dumps(params), status=status.HTTP_401_UNAUTHORIZED)
    else:
        params = {}
        return HttpResponse(json.dumps(params), status=status.HTTP_404_NOT_FOUND)


def show_list(request):
    all_users = UserInfo.objects.all()
    params = []
    for user in all_users:
        username = user.username
        print(username)
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
