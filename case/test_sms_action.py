import json
import unittest
from api.api_request_method import ApiSearch
from tools.read_excel import ReadExcel
from config.log import logger  # 引入全局日志对象


class TestSearch(unittest.TestCase):

    def test_sms_action_login(self):
        params = ReadExcel.read_excel()
        for index, param in enumerate(params):
            if param['接口名称'] == '登录验证码':
                response =  ApiSearch.api_post(param['请求地址'], json.loads(param['请求参数']))
                data = [response.json()]
                ReadExcel.write_excel_to_cell(data, sheet_name='Sheet1', startrow=index + 1, startcol=9)
                print(f'\n接口名称：{param["接口名称"]}, 用例名称：{param["用例名称"]}，返回值：{response.json()}')
            else:
                pass

    def test_sms_action_register(self):
        params = ReadExcel.read_excel()
        for index, param in enumerate(params):
            if param['接口名称'] == '注册验证码':
                response = ApiSearch.api_post(param['请求地址'], json.loads(param['请求参数']))
                print(f'\n接口名称: {param["接口名称"]}，用例名称：{param["用例名称"]}，返回值：{response.json()}')
                data = [response.json()]
                logger.info(f'用例名称：{param["用例名称"]}，返回值：{response.json()}')# 使用全局日志对象
                ReadExcel.write_excel_to_cell(data, sheet_name='Sheet1', startrow=index + 1, startcol=9)
            else:
                pass


