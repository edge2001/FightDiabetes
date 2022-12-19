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
from user.utils.token import get_username


# add a sports record
def add_sports_record(request):
    if request.method == 'POST':
        body = request.body.decode('UTF-8')
        content = json.loads(body)
        sport_type = content['sport_type']
        datetime = content['datetime']
        notes = content['notes']
        token = request.META.get('HTTP_TOKEN')
        username = get_username(token)
        user = UserInfo.objects.get(username=username)
        new_record = Sports_record(sport_type = sport_type, notes = notes, user = user, datetime = datetime)
        new_record.save()
        params = {}
        return HttpResponse(json.dumps(params),status = status.HTTP_200_OK)

def get_sports_data(request):
    if request.method == 'GET':
        token = request.META.get('HTTP_TOKEN')
        username = get_username(token)

        # body = request.body.decode('UTF-8')
        # content = json.loads(body)
        # username = content['username']

        user = UserInfo.objects.get(username=username)
        params = {
            'dates' : []
        }
        records = user.user_sports_record.filter()
        for i in range(len(records)):
            new_date = records[i].datetime
            new_date = new_date.strftime('%Y/%m/%d')
            print(new_date)
            if new_date in params['dates']:
                continue
            else:
                params['dates'].append(new_date)

        return HttpResponse(json.dumps(params), status = status.HTTP_200_OK)






#获取吃药时间
def getMedicineTime(request):
    if request.method == 'GET':
        dict = {
            'list':[
                {
                    'hour' : '12',
                    'minute':'12'
                },
                {
                    'hour' : '20',
                    'minute':'47'
                }
            ]
        }
        return HttpResponse(json.dumps(dict), status=status.HTTP_200_OK)



