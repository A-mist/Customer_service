import pytest
import requests
import json
from datetime import datetime

class TestLoginAPI:
    def setup_class(self):
        """测试类的初始化配置"""
        self.base_url = "https://test-tooduduapi.ptdplat.com/api/app"
        self.headers = {"Content-Type": "application/json"}
        
    @pytest.mark.login
    def test_valid_login(self):
        """测试用例1: 使用有效账号密码登录"""
        url = f"{self.base_url}/login-by-phone"
        payload = {
            "username": "test_user",
            "password": "test_password123"
        }
        
        response = requests.post(
            url=url,
            json=payload,
            headers=self.headers
        )
        
        # 断言状态码
        assert response.status_code == 200
        
        # 断言响应数据
        resp_data = response.json()
        assert resp_data.get("code") == 200
        assert "token" in resp_data
        assert len(resp_data["token"]) > 0
        
    @pytest.mark.login
    def test_invalid_password(self):
        """测试用例2: 使用错误密码登录"""
        url = f"{self.base_url}/login-by-phone"
        payload = {
            "username": "test_user",
            "password": "wrong_password"
        }
        
        response = requests.post(
            url=url,
            json=payload,
            headers=self.headers
        )
        
        assert response.status_code == 401
        resp_data = response.json()
        assert resp_data.get("code") == 401
        assert "密码错误" in resp_data.get("message", "")
        
    @pytest.mark.login
    def test_empty_username(self):
        """测试用例3: 用户名为空"""
        url = f"{self.base_url}/login-by-phone"
        payload = {
            "username": "",
            "password": "test_password123"
        }
        
        response = requests.post(
            url=url,
            json=payload,
            headers=self.headers
        )
        
        assert response.status_code == 400
        resp_data = response.json()
        assert resp_data.get("code") == 400
        assert "用户名不能为空" in resp_data.get("message", "")

    @pytest.mark.login
    def test_invalid_request_method(self):
        """测试用例4: 使用错误的HTTP方法"""
        url = f"{self.base_url}/login-by-phone"
        
        response = requests.get(url, headers=self.headers)
        
        assert response.status_code == 405
        
    @pytest.mark.login
    def test_invalid_content_type(self):
        """测试用例5: 使用错误的Content-Type"""
        url = f"{self.base_url}/login-by-phone"
        payload = "username=test_user&password=test_password123"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        
        response = requests.post(
            url=url,
            data=payload,
            headers=headers
        )
        
        assert response.status_code == 415

    def _log_test_result(self, response, test_name):
        """记录测试结果"""
        print(f"\n=== {test_name} ===")
        print(f"Request URL: {response.request.url}")
        print(f"Request Method: {response.request.method}")
        print(f"Request Headers: {response.request.headers}")
        print(f"Request Body: {response.request.body}")
        print(f"Response Status: {response.status_code}")
        print(f"Response Body: {response.text}")
        print("=" * 50)

if __name__ == "__main__":
    pytest.main(["-v", "-s", "--html=report.html"])