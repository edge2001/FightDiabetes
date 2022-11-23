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


# 添加健康数据
def add_datum(request):
    if request.method == 'POST':
        blood_glucose = request.POST.get('blood_glucose')
        weight = request.POST.get('weight')
        ketone = request.POST.get('ketone')
        time_tag = request.POST.get('time_tag')
        notes = request.POST.get('notes')
        newdatum = datum(blood_glucose = blood_glucose, weight = weight, ketone = ketone,time_tag = time_tag, notes = notes)
        # newdatum.user = 当前用户
        newdatum.save()