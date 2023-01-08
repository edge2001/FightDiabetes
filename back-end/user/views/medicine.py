
import json

import pytz
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from user.models import Medicine_record, Sports_record, UserInfo, MedicineTime
from user.utils.token import get_username

LOCAL_TIME_ZONE = pytz.timezone('Asia/Shanghai')

# add a sports record


def add_medicine_record(request):
    if request.method == 'POST':
        body = request.body.decode('UTF-8')
        content = json.loads(body)
        medicine_type = content['medicine_type']
        datetime = content['datetime']
        notes = content['notes']
        quantity = content['quantity']
        token = request.META.get('HTTP_TOKEN')
        username = get_username(token)
        user = UserInfo.objects.get(username=username)
        new_record = Medicine_record(
            medicine_type=medicine_type,
            notes=notes,
            quantity=quantity,
            user=user,
            datetime=datetime)
        new_record.save()
        params = {}
        return HttpResponse(json.dumps(params), status=status.HTTP_200_OK)


def get_medicine_data(request):
    if request.method == 'GET':
        token = request.META.get('HTTP_TOKEN')
        username = get_username(token)

        # body = request.body.decode('UTF-8')
        # content = json.loads(body)
        # username = content['username']

        user = UserInfo.objects.get(username=username)
        params = {
            'dates': []
        }
        records = user.user_medicine_record.filter()
        for i in range(len(records)):
            new_date = records[i].datetime.astimezone(LOCAL_TIME_ZONE)
            new_date = new_date.strftime('%Y/%m/%d')
            print(new_date)
            if new_date in params['dates']:
                continue
            else:
                params['dates'].append(new_date)

        return HttpResponse(json.dumps(params), status=status.HTTP_200_OK)


def setMedicineTime(request):
    if request.method == 'POST':
        body = request.body.decode('UTF-8')
        content = json.loads(body)
        hour = int(content['hour'])
        minute = int(content['minute'])
        token = request.META.get('HTTP_TOKEN')
        username = get_username(token)
        user = UserInfo.objects.get(username=username)

        new_time = MedicineTime(
            hour=hour,
            minute=minute,
            user=user)
        new_time.save()
        print(new_time.hour)
        params = {
            'hour': hour,
            'minute': minute
        }
        return HttpResponse(json.dumps(params), status=status.HTTP_200_OK)


# 获取吃药时间
def getMedicineTime(request):
    if request.method == 'GET':
        token = request.META.get('HTTP_TOKEN')
        username = get_username(token)
        user = UserInfo.objects.get(username=username)
        times = user.user_medicinetime.filter()
        timeList = []
        for i in range(len(times)):
            hour = times[i].hour
            minute = times[i].minute
            js = {
                "hour": hour,
                "minute": minute
            }
            timeList.append(js)
        dict = {
            'list': timeList,
        }
        return HttpResponse(json.dumps(dict), status=status.HTTP_200_OK)
