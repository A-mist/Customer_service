from http.client import responses

import requests

from tools.read_excel import ReadExcel


class ApiSearch(object):
        @staticmethod
        def api_search(url, data):
            headers = {
                "User-Agent": "",
                "Content-Type": "application/json"
            }

            response = requests.post(url, headers=headers, json=data)
            return response

        @staticmethod
        def api_search_type(url, data):
            headers = {
                "User-Agent": "",
                "Content-Type": "application/json"
            }
            response=requests.get(url=url, headers=headers,json=data)
            return response



