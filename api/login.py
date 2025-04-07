"""
登录接口对象封装
"""
from http.client import responses

import requests



class LoginAPI(object):
    @staticmethod
    def api_login(
            url: str = "http://laravel-shop.ptdmeta.cn/api/v1/auth/login-by-password",
            account:   str = "admin" ,
            password:str="Aa123456"
    )->requests.Response:

        headers = {
            "User-Agent": "",
            "Content-Type": "application/json"
        }
        data = {
            "account": account,
            "password": password
        }
        responses = requests.post(url, headers=headers, json=data)

        print(responses.status_code)


if __name__ == '__main__':
    LoginAPI.api_login()
