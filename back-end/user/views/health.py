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


# 添加单条健康数据
def add_datum(request):
    if request.method == 'POST':
        blood_glucose = request.POST.get('blood_glucose')
        weight = request.POST.get('weight')
        ketone = request.POST.get('ketone')
        time_tag = request.POST.get('time_tag')
        notes = request.POST.get('notes')
        newdatum = datum(blood_glucose=blood_glucose, weight=weight,
                         ketone=ketone, time_tag=time_tag, notes=notes)
        dict = request.session['info']
        username = dict['username']
        user = UserInfo.objects.get(username=username)
        newdatum.user = user
        newdatum.save()

# 返回某天的血糖数据


def get_day_glucose(request):
    if request.method == 'POST':
        # 获取当前用户信息
        dict = request.session['info']
        username = dict['username']
        user = UserInfo.objects.get(username=username)
        # 获取所需日期，days为返回的据今天的天数，0为今天
        days = request.POST.get('days')
        today = datetime.date.today()
        date = today - datetime.timedelta(days=days)
        data = user.user_data.filter(date=date)
        # 返回的数组，day_glucose[1]为早上空腹时
        day_glucose = []
        for i in range(0, 7):
            day_glucose[i] = 0

        for time_datum in data:
            i = time_datum.time_tag
            j = time_datum.blood_glucose
            day_glucose[i] = j
        dict = {
            'day_glucose': day_glucose,
        }
        return HttpResponse(dict, status=status.HTTP_200_OK)


# 返回过去七天某个time_tag的血糖值
# glucose[0]返回距今第6天的
def get_week_glucose(request):
    if request.method == 'POST':
        # 获取当前用户信息
        dict = request.session['info']
        username = dict['username']
        user = UserInfo.objects.get(username=username)
        # 获取需要查询的时段
        time_tag = request.POST.get('time_tag')

        glucose = []
        for i in range(0, 7):
            glucose[i] = 0
        today = datetime.date.today()
        for i in range(0, 6):
            date = today - datetime.timedelta(days=(6-i))
            try:
                datum = user.user_data.get(date=date, time_tag=time_tag)
                glu = datum.blood_glucose
                glucose[i] = glu
            except:
                pass
            continue

        # 初始化要返回的dict
        dict = {
            'glucose': glucose,
        }
        return HttpResponse(dict, status=status.HTTP_200_OK)


# 返回过去一个月某个time_tag的血糖值
# glucose[0]返回距今第29天的
def get_month_glucose(request):
    if request.method == 'POST':
        # 获取当前用户信息
        dict = request.session['info']
        username = dict['username']
        user = UserInfo.objects.get(username=username)
        # 获取需要查询的时段
        time_tag = request.POST.get('time_tag')

        glucose = []
        for i in range(0, 30):
            glucose[i] = 0
        today = datetime.date.today()
        for i in range(0, 29):
            date = today - datetime.timedelta(days=(29-i))
            try:
                datum = user.user_data.get(date=date, time_tag=time_tag)
                glu = datum.blood_glucose
                glucose[i] = glu
            except:
                pass
            continue

        # 初始化要返回的dict
        dict = {
            'glucose': glucose,
        }
        return HttpResponse(dict, status=status.HTTP_200_OK)


# 获取最近一周的统计数据
# 返回值：总测试次数time, 正常次数normal_time,偏高次数above_time,偏低次数below_time(目前仅统计空腹时)
# 血糖最值max,min,分六个时段的平均值av1,av2...
def get_week_statistics(request):
    if request.method == 'GET':
        # 获取当前用户信息
        dict = request.session['info']
        username = dict['username']
        user = UserInfo.objects.get(username=username)

        # 获取过去七天date的列表
        dates = []
        today = datetime.date.today()
        for i in range(6, 0, -1):
            date = today - datetime.timedelta(days=i)
            dates.append(date)
        dates.append(today)

        # 初始化需返回的数据
        min = 10000
        max = -1
        time = 0
        above_time = 0
        below_time = 0
        normal_time = 0
        av1 = 0
        num1 = 0
        av2 = 0
        num2 = 0
        av3 = 0
        num3 = 0
        av4 = 0
        num4 = 0
        av5 = 0
        num5 = 0
        av6 = 0
        num6 = 0
        for date in dates:
            data = user.user_data.filter(date=date)
            for datum in data:
                blood_glucose = datum.blood_glucose
                if blood_glucose > max:
                    max = blood_glucose
                if blood_glucose < min:
                    min = blood_glucose
                t = datum.time_tag
                if t == 1:
                    av1 += blood_glucose
                    num1 += 1
                    time += 1
                    if blood_glucose < 3.9:
                        below_time += 1
                    elif blood_glucose > 6.1:
                        above_time += 1
                    else:
                        normal_time += 1
                elif t == 2:
                    av2 += blood_glucose
                    num2 += 1
                elif t == 3:
                    av3 += blood_glucose
                    num3 += 1
                    time += 1
                    if blood_glucose < 3.9:
                        below_time += 1
                    elif blood_glucose > 6.1:
                        above_time += 1
                    else:
                        normal_time += 1
                elif t == 4:
                    av4 += blood_glucose
                    num4 += 1
                elif t == 5:
                    av5 += blood_glucose
                    num5 += 1
                    time += 1
                    if blood_glucose < 3.9:
                        below_time += 1
                    elif blood_glucose > 6.1:
                        above_time += 1
                    else:
                        normal_time += 1
                elif t == 6:
                    av6 += blood_glucose
                    num6 += 1
        av1 = av1 / num1
        av2 = av2 / num2
        av3 = av3 / num3
        av4 = av4 / num4
        av5 = av5 / num5
        av6 = av6 / num6
        dict = {
            'min': min,
            'max': max,
            'time': time,
            'av1': av1,
            'av2': av2,
            'av3': av3,
            'av4': av4,
            'av5': av5,
            'av6': av6,
            'time': time,
            'normal_time': normal_time,
            'above_time': above_time,
            'below_time': below_time,
        }
        return HttpResponse(dict, status=status.HTTP_200_OK)


# 获取最近一月的统计数据
# 返回值：总测试次数time, 正常次数normal_time,偏高次数above_time,偏低次数below_time(目前仅统计空腹时)
# 血糖最值max,min,分六个时段的平均值av1,av2...
def get_month_statistics(request):
    if request.method == 'GET':
        print(request.session.items())
        # 获取当前用户信息
        dict = request.session['info']
        username = dict['username']
        user = UserInfo.objects.get(username=username)

        # 获取过去七天date的列表
        dates = []
        today = datetime.date.today()
        for i in range(29, 0, -1):
            date = today - datetime.timedelta(days=i)
            dates.append(date)
        dates.append(today)

        # 初始化需返回的数据
        min = 10000
        max = -1
        time = 0
        above_time = 0
        below_time = 0
        normal_time = 0
        av1 = 0
        num1 = 0
        av2 = 0
        num2 = 0
        av3 = 0
        num3 = 0
        av4 = 0
        num4 = 0
        av5 = 0
        num5 = 0
        av6 = 0
        num6 = 0
        for date in dates:
            data = user.user_data.filter(date=date)
            for datum in data:
                blood_glucose = datum.blood_glucose
                if blood_glucose > max:
                    max = blood_glucose
                if blood_glucose < min:
                    min = blood_glucose
                t = datum.time_tag
                if t == 1:
                    av1 += blood_glucose
                    num1 += 1
                    time += 1
                    if blood_glucose < 3.9:
                        below_time += 1
                    elif blood_glucose > 6.1:
                        above_time += 1
                    else:
                        normal_time += 1
                elif t == 2:
                    av2 += blood_glucose
                    num2 += 1
                elif t == 3:
                    av3 += blood_glucose
                    num3 += 1
                    time += 1
                    if blood_glucose < 3.9:
                        below_time += 1
                    elif blood_glucose > 6.1:
                        above_time += 1
                    else:
                        normal_time += 1
                elif t == 4:
                    av4 += blood_glucose
                    num4 += 1
                elif t == 5:
                    av5 += blood_glucose
                    num5 += 1
                    time += 1
                    if blood_glucose < 3.9:
                        below_time += 1
                    elif blood_glucose > 6.1:
                        above_time += 1
                    else:
                        normal_time += 1
                elif t == 6:
                    av6 += blood_glucose
                    num6 += 1
        av1 = av1 / num1
        av2 = av2 / num2
        av3 = av3 / num3
        av4 = av4 / num4
        av5 = av5 / num5
        av6 = av6 / num6
        dict = {
            'min': min,
            'max': max,
            'time': time,
            'av1': av1,
            'av2': av2,
            'av3': av3,
            'av4': av4,
            'av5': av5,
            'av6': av6,
            'time': time,
            'normal_time': normal_time,
            'above_time': above_time,
            'below_time': below_time,
        }
        return HttpResponse(dict, status=status.HTTP_200_OK)
