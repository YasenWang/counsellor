from django.shortcuts import render

# Create your views here.
import logging
from dingtalk_robot.AppManager import AppManager
from dingtalk_robot.MessageSender import MessageSender
from django.http import HttpResponse
import requests


def dingtalk_robot(request):

    return HttpResponse('success!')


