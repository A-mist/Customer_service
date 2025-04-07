from pandas import read_excel

import data.config as data
import pandas as pd
import os

class  ReadExcel(object):
    @staticmethod
    def read_excel_id():
        if not os.path.exists(data.excel_path):
            print(f"文件路径错误或文件不存在: {data.excel_path}")
            return
        try:
            df = pd.read_excel(data.excel_path, engine='openpyxl')
            for index, row in df.iterrows():
                line = row['ID']
                yield line
        except Exception as e:
            print(f"读取文件时出错: {e}")

    @staticmethod
    def read_excel_module():
        if not os.path.exists(data.excel_path):
            print(f"文件路径错误或文件不存在: {data.excel_path}")
            return
        try:
            df = pd.read_excel(data.excel_path, engine='openpyxl')
            for index, row in df.iterrows():
                line = row['模块']
                yield line
        except Exception as e:
            print(f"读取文件时出错: {e}")

    @staticmethod
    def read_excel_interface_name():
        if not os.path.exists(data.excel_path):
            print(f"文件路径错误或文件不存在: {data.excel_path}")
            return
        try:
            df = pd.read_excel(data.excel_path, engine='openpyxl')
            for index, row in df.iterrows():
                line = row['接口名称']
                yield line
        except Exception as e:
            print(f"读取文件时出错: {e}")

    @staticmethod
    def read_excel_request_address():
        if not os.path.exists(data.excel_path):
            print(f"文件路径错误或文件不存在: {data.excel_path}")
            return
        try:
            df = pd.read_excel(data.excel_path, engine='openpyxl')
            for index, row in df.iterrows():
                line = row['请求地址']
                yield line
        except Exception as e:
            print(f"读取文件时出错: {e}")


    @staticmethod
    def read_excel_case_name():
        if not os.path.exists(data.excel_path):
            print(f"文件路径错误或文件不存在: {data.excel_path}")
            return
        try:
            df = pd.read_excel(data.excel_path, engine='openpyxl')
            for index, row in df.iterrows():
                line = row['用例名称']
                yield line
        except Exception as e:
            print(f"读取文件时出错: {e}")


    @staticmethod
    def read_excel_request_method():
        if not os.path.exists(data.excel_path):
            print(f"文件路径错误或文件不存在: {data.excel_path}")
            return
        try:
            df = pd.read_excel(data.excel_path, engine='openpyxl')
            for index, row in df.iterrows():
                line = row['请求方法']
                yield line
        except Exception as e:
            print(f"读取文件时出错: {e}")


    @staticmethod
    def read_excel_parameter_typ ():
        if not os.path.exists(data.excel_path):
            print(f"文件路径错误或文件不存在: {data.excel_path}")
            return
        try:
            df = pd.read_excel(data.excel_path, engine='openpyxl')
            for index, row in df.iterrows():
                line = row['请求参数类型']
                yield line
        except Exception as e:
            print(f"读取文件时出错: {e}")


    @staticmethod
    def read_excel_request_parameter():
        if not os.path.exists(data.excel_path):
            print(f"文件路径错误或文件不存在: {data.excel_path}")
            return
        try:
            df = pd.read_excel(data.excel_path, engine='openpyxl')
            for index, row in df.iterrows():
                line = row['请求参数']
                yield line
        except Exception as e:
            print(f"读取文件时出错: {e}")


    @staticmethod
    def read_excel_expected_result():
        if not os.path.exists(data.excel_path):
            print(f"文件路径错误或文件不存在: {data.excel_path}")
            return
        try:
            df = pd.read_excel(data.excel_path, engine='openpyxl')
            for index, row in df.iterrows():
                line = row['预期结果']
                yield line
        except Exception as e:
            print(f"读取文件时出错: {e}")


    @staticmethod
    def read_excel_test_result():
        if not os.path.exists(data.excel_path):
            print(f"文件路径错误或文件不存在: {data.excel_path}")
            return
        try:
            df = pd.read_excel(data.excel_path, engine='openpyxl')
            for index, row in df.iterrows():
                line = row['测试结果']
                yield line
        except Exception as e:
            print(f"读取文件时出错: {e}")


    @staticmethod
    def read_excel():
        if not os.path.exists(data.excel_path):
            print(f"文件路径错误或文件不存在: {data.excel_path}")
            return
        try:
            df = pd.read_excel(data.excel_path, engine='openpyxl')
            for index, row in df.iterrows():
                line = row
                yield line

        except Exception as e:
            print(f"读取文件时出错: {e}")



