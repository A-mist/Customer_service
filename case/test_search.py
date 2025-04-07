import unittest
from tkinter.font import names

from api.search import ApiSearch
from tools.read_excel import ReadExcel


class TestSearch(unittest.TestCase):
    def test_search(self):
        params = ReadExcel.read_excel()
        for index, param in enumerate(params):
            print(param)
            if param['接口名称'] == '搜索':
                response =  ApiSearch.api_search(param['请求地址'], param['请求参数'])
                # print(response.text)

                # self.assertEqual(200, response.status_code)
                # self.assertEqual("手机", "手机")

    def test_search_type(self):
        params = ReadExcel.read_excel()
        for index, param in enumerate(params):
            if param['接口名称'] == '搜索':
                response =  ApiSearch.api_search(param['请求地址'], param['请求参数'])
                print('\n',param['请求地址'],'\n', param['请求参数'])
                print(response.status_code)
            # response =  ApiSearch.api_search_type(param,)
            # data = response.json().get("data")
            # name = [item["name"] for item in data]
            # self.assertEqual(200, response.status_code)
            # self.assertIn("电子产品", name)


