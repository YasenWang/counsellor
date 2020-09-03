# -*- coding:utf-8 -*-
# Time:     2020/8/23 13:24
# Author:   Yasen Wang
# Email:    my@wangyusheng.cn
# File:     MessageSender.py
from django.http import HttpResponse
from dingtalk_robot import AppManager
import hmac
import hashlib
import base64
import urllib.parse
import time
import requests


class MessageSender(object):
    def __init__(self, web_hook, secret, app_manager=''):
        self.web_hook = web_hook
        self.secret = secret
        self.app_manager = app_manager

    def __get_sign(self):
        timestamp = str(round(time.time() * 1000))
        secret_enc = self.secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return timestamp, sign

    def send_text_msg(self, msg, at='', is_at_all=False):
        header = {
            'Content-Type': 'application/json',
            'charset': 'utf-8',
            'Data-Type': 'json'
        }
        if is_at_all:
            is_at_all_str = 'true'
        else:
            is_at_all_str = 'false'
        data = '''{{
                    "msgtype": "text",
                    "text":{{
                        "content": "{0}"
                    }},
                    "at": {{
                        "atMobiles": [
                            "{1}"
                        ], 
                        "isAtAll": {2}
                    }}
        }}'''.format(msg, at, is_at_all_str)
        timestamp, sign = self.__get_sign()
        web_hook = '{}' \
                   '&timestamp={}&sign={}'.format(self.web_hook, timestamp, sign)
        res = requests.post(web_hook,
                            headers=header,
                            data=data)
        return res.text


if __name__ == '__main__':
    am = AppManager
    result = MessageSender(web_hook='https://oapi.dingtalk.com/robot/send?'
                                    'access_token=1819614d9b73207823afecfe686736189f575c25bf367f3f3d821f9d906f5c67',
                           secret='SEC270fd2c049a7540cae4e8f9f251ef36c5db52ff64bbdf95d34db6e88863a3dee')\
        .send_text_msg('test', is_at_all=True)
    print(result)

