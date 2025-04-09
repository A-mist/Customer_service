import json
import unittest
from api.api_request_method import ApiSearch
from tools.read_excel import ReadExcel


class TestSearch(unittest.TestCase):

    def test_sms_action_login(self):
        params = ReadExcel.read_excel()
        for index, param in enumerate(params):
            if param['接口名称'] == '登录验证码':
                response =  ApiSearch.api_post(param['请求地址'], json.loads(param['请求参数']), param[''])
                print(f'\n接口名称：{param["接口名称"]}, 用例名称：{param["用例名称"]}，返回值：{response.json()}')
                data = [response.json()]
                ReadExcel.write_excel_to_cell(data, sheet_name='Sheet1', startrow=index + 1, startcol=9)
            else:
                pass

    def test_sms_action_password_forget(self):
        params = ReadExcel.read_excel()
        for index, param in enumerate(params):
            if param['接口名称'] == '忘记密码验证码':
                response = ApiSearch.api_post(param['请求地址'], json.loads(param['请求参数']))
                print(f'\n接口名称: {param["接口名称"]}，用例名称：{param["用例名称"]}，返回值：{response.json()}')
                data = [response.json()]
                ReadExcel.write_excel_to_cell(data, sheet_name='Sheet1', startrow=index + 1, startcol=9)
            else:
                pass


    def test_sms_action_password_edit(self):
        params = ReadExcel.read_excel()
        for index, param in enumerate(params):
            if param['接口名称'] == '修改密码验证码':
                response = ApiSearch.api_post(param['请求地址'], json.loads(param['请求参数']))
                print(f'\n接口名称: {param["接口名称"]}，用例名称：{param["用例名称"]}，返回值：{response.json()}')
                data = [response.json()]
                ReadExcel.write_excel_to_cell(data, sheet_name='Sheet1', startrow=index + 1, startcol=9)
            else:
                pass


    def test_sms_action_phone_edit(self):
        params = ReadExcel.read_excel()
        for index, param in enumerate(params):
            if param['接口名称'] == '修改手机号验证码':
                response = ApiSearch.api_post(param['请求地址'], json.loads(param['请求参数']))
                print(f'\n接口名称: {param["接口名称"]}，用例名称：{param["用例名称"]}，返回值：{response.json()}')
                data = [response.json()]
                ReadExcel.write_excel_to_cell(data, sheet_name='Sheet1', startrow=index + 1, startcol=9)
            else:
                pass


    def test_sms_action_phone_verify(self):
        params = ReadExcel.read_excel()
        for index, param in enumerate(params):
            if param['接口名称'] == '修改手机号之前的验证手机号验证码':
                response = ApiSearch.api_post(param['请求地址'], json.loads(param['请求参数']))
                print(f'\n接口名称: {param["接口名称"]}，用例名称：{param["用例名称"]}，返回值：{response.json()}')
                data = [response.json()]
                ReadExcel.write_excel_to_cell(data, sheet_name='Sheet1', startrow=index + 1, startcol=9)
            else:
                pass





