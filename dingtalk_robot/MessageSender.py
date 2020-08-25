# -*- coding:utf-8 -*-
# Time:     2020/8/23 13:24
# Author:   Yasen Wang
# Email:    my@wangyusheng.cn
# File:     MessageSender.py
from django.http import HttpResponse
from dingtalk_robot import AppManager


class MessageSender(object):
    def __init__(self, AppManager):
        self.appmanager = AppManager
        self.data = ''

    def getTextSender(self, text_message, at='', is_at_all=False):
        self.data = '''{{
            "msgtype": "text",
            "text":{{{0}}},
            "at": {{
                "atMobiles": [
                    "{1}"
                ], 
                "isAtAll": {2}
            }}
        }}'''
        self.data = self.data.format(text_message, at, is_at_all)
        return self


if __name__ == '__main__':
    s1 = MessageSender('AppManager()').getTextSender('aaa', at='13261770011', is_at_all=False)
