import requests



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


        @staticmethod
        def api_put(url, data):
            headers = {
                "User-Agent": "",
                "Content-Type": "application/json"
            }
            response=requests.put(url, json=data, headers=headers)
            return response



