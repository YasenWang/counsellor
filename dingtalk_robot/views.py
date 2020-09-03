from django.shortcuts import render

# Create your views here.
import logging
from dingtalk_robot.AppManager import AppManager
from dingtalk_robot.MessageSender import MessageSender
from django.http import HttpResponse
import requests


def dingtalk_robot(request):
    am = AppManager(2784001, 'dingekcnjw1fgxyc5lee', 'pmtnRMPZfHFI9kGU9mcIUbJbGvvY_1KG3U5HAf5Cz02lIi-TZ6JZLr0Ye7bPGvN2')
    ms = MessageSender(am).get_text_sender('收到消息')
    return HttpResponse(ms.data)


