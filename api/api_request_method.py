from http.client import responses

import requests

from tools.read_excel import ReadExcel


class ApiSearch(object):
        @staticmethod
        def api_post(url, data):
            headers = {
                "User-Agent": "",
                "Content-Type": "application/json"
            }

            response = requests.post(url, data)
            return response

        @staticmethod
        def api_get(url):
            headers = {
                "User-Agent": "",
                "Content-Type": "application/json"
            }
            response=requests.get(url)
            return response



