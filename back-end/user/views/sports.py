from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

import datetime
import threading
from rest_framework import status
from rest_framework.response import Response
import json
from user.models import UserInfo, Sports_record

# add a sports record


def add_record(request):
    if request.method == 'POST':
        body = request.body.decode('UTF-8')
        content = json.loads(body)
        sport_type = content['sport_type']
        notes = content['notes']
        info = request.session['info']
        username = info['username']
        user = UserInfo.objects.get(username=username)
        new_record = Sports_record(
            sport_type=sport_type, notes=notes, user=user)
        new_record.save()
        params = {}
        return HttpResponse(json.dumps(params), status=status.HTTP_200_OK)


# 获取吃药时间
def getMedicineTime(request):
    if request.method == 'GET':
        dict = {
            'list': [
                {
                    'hour': '12',
                    'minute': '12'
                },
                {
                    'hour': '21',
                    'minute': '13'
                }
            ]
        }
        return HttpResponse(json.dumps(dict), status=status.HTTP_200_OK)
