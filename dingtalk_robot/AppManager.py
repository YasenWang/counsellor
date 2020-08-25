# -*- coding:utf-8 -*-
# Time:     2020/8/22 21:05
# Author:   Yasen Wang
# Email:    my@wangyusheng.cn
# File:     AppManager.py
import hmac
import hashlib
import base64


class AppManager(object):
    def __init__(self, agent_id, app_key, app_secret):
        self.agent_id = agent_id
        self.app_key = app_key
        self.app_secret = app_secret

    def get_sign(self, timestamp):
        app_secret_enc = self.app_secret.encode('utf-8')
        string_to_sign_enc = '{}\n{}'.format(timestamp, self.app_secret).encode('utf-8')
        hmac_code = hmac.new(app_secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = base64.b64encode(hmac_code).decode('utf-8')
        return sign

