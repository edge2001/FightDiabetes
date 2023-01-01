
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from user.models import UserInfo, datum
