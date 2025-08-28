
import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
import hashlib
import json
import time
import urllib

def md5_encrypt(password):
    """
    对密码进行MD5加密
    """
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


def generate_sign(paras, api_key):
    """
    参数加密生成签名

    :param paras: 请求参数字典
    :param api_key: 用于签名的密钥
    :return: 包含签名和时间戳的参数字典
    """
    # 深拷贝参数字典，避免修改原始数据
    params = paras.copy()

    # 添加时间戳
    params['timeStamp'] = '%d' % int(time.time())

    # 过滤参数
    for k in list(params.keys()):
        if ('' == params[k] or params[k] is None or 'file' == k):
            del params[k]

    # 参数排序
    sorted_params = dict(sorted(params.items(), key=lambda e: e[0], reverse=False))

    # 生成参数字符串
    params_str = urllib.parse.unquote(urllib.parse.urlencode(sorted_params, doseq=True)) + api_key

    # 生成md5 sign
    md5_str = hashlib.md5(params_str.encode(encoding='UTF-8')).hexdigest()

    # 将签名和时间戳加入参数
    params['sign'] = md5_str
    params['timeStamp'] = int(time.time())

    return params

def encrypt_password(password):
    public_key = "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDKNDkSrArS4rzj\ngxAS5cO4c3t8QPz9A+G8C/0vLvBbAtO6dwaoi+u3KIdQd75yJTld0Kdg9P553qUt\n7ABVHNUjbOUu3lM+LKgOlTlmzWZwH/j6S54ktgyxJ1biRsB484FmuHnvkE/kYdPV\nWDmdhIi2xzJFZJzeSZLIuywvbjf8BmhuOrv+8p51FgrSF994CWGqKWK0WXRUhdhY\nCgu9Yy6ZgudH5xmO+gXcK+DJ92WiEKRC80gcM9pAajCSUjlBPVWUu+3pfVy1qA3Q\nNNmQRIzxjM0L+Awzbg4+cyNG9rc5WR/xrdBEpnFJ5I53hmsU07s9oEpR8PsomRM0\nL+n/lEslAgMBAAECggEAUbivhFth+H9I5g6XVXvlEUwjEUHWvY9vESgrSIGJBM9s\nsQTf/Qin2JuZrKzonIts1vy4WRhLLQgN7DRgogWIIswlCD80l4FG3rXywBitmQ1i\n/A3JuX6WPJbwp3z+1yNbHh/asDa8A0qCacxBZOcmtfBl4ePa/n/vwg7bucOq/sED\nKY7E161oXHDlBVoFD8Q8JuTKYMbKcqzAE3YAgIUwnRfp1oLa6UpMWHRBDBrMb7S+\nFRjLwyB4FUthzEVqrMWHMJfC02I9QDt72gCjumOkUWWZtfxb7m7r2I72Sbx08CyO\n4in+6RzM54Za1xMWsRwaOo/+1eRXvwzbs9VEtmtmNQKBgQD+s7X1xp7MBfvpmLAq\n1K/BbxJHOndPtT89mDGYQ8GkfX1o1cKhdN9CSv6LrXpf6U4Y0FW0KUeXBhvvsUiL\nFkCLcutqSoclPYr9a4MVXKs67m268Bq1zypM8Y+KYQrvdOCpqN/cIEffjTevJmEq\nGbc8I1vyANrFqhmNxk1Z6xZhwwKBgQDLPAWxhc9tyGy0P2WnEgDQXKNxNbulDDqQ\nbM1Trnap6iT0Xao/6FY6LglB5MBJThWUbZw084Ke7sSt4resHfnrXogAm95KFGQy\n0NejD0El98Z6rgUUy+e4m1VAOTyfXu8GBF3xo0P6+jNvrkKNEo0cdrE878HdbnK8\nlNXxzpyo9wKBgAODZxckzjvyOS9Xs9ZjaKk6Zv4kiFDJJz4qQ0TeamVidcBkcnLX\nsdywPCKhGfcIuNMOzJ/Xke07YFdGEsIYZHuH8kddD9ArsScdvIkm5hXCBDF37mZj\nnSnCi0BVZlk3O4IbmjrnFxa2U/ZOiTiTcjuaIUKNUHc5iXCzM43x+DURAoGBAJT2\ndaXc0mFBWovzO+rtQzN180ZzgApFoFdjqEwBwHBicpu6W6NkBG+4doiZxmb0mNSm\nUqxtH/ymPfrGBqJdhmWCcGUh2hiqQZcNhEC8WaAesJgTHR5VJo8lK6NbUJfv2Xqr\nkMAgTx+SbEkbjSQhyNRoGxjzE0HeRrL61KXcLu+ZAoGBAPNEtAuIvBQoc4Uh77wK\nXQ7Z7PFHXe/rCz/KET3sPKZ8blKX+0slp47k9ErSP8JNamaHdWhk3/x2qE6kU9q0\nqp6nFquR9Y128YOC37TpiAm+oQJxe7GwGQsXdNHJ0wiFVXlS7tnRbsn5LywRYNvI\nbtdLiM0EXtw+yBE6SsHRVEx2\n-----END PRIVATE KEY-----\n"
    try:
        key = RSA.importKey(public_key)
        cipher = PKCS1_v1_5.new(key)
        encrypted = cipher.encrypt(password.encode('utf-8'))
        return base64.b64encode(encrypted).decode('utf-8')
    except Exception as e:
        print(f"RSA加密失败: {e}")
        return None


def test_longin():
    login_url = "https://test-toodudu.ptdplat.com/login"
    login_res = requests.post(login_url, data={"name": "李龙威",
                                   "password": encrypt_password("a123456")
                                   }
                        )

    print("登录响应状态码:", login_res.status_code)
    if login_res.status_code != 200:
        print("登录失败:", login_res.text)
        return  None
    # 从登录响应中提取token（需要根据实际响应结构调整）
    if login_res.status_code == 200:
        try:
            response_data = login_res.headers
            headers = response_data
            print("获取到的headers:", headers)

            # 检查headers是否为空
            if headers:
                # 创建要保存的数据
                token_data = {
                    "headers": dict(headers),  # 转换为普通字典
                }

                import os

                # 将token写入JSON文件
                with open("token.json", "w", encoding="utf-8") as f:
                    json.dump(token_data, f, ensure_ascii=False, indent=2)
                    print("文件写入完成!")

                print("Token已成功保存到token.json文件中")
                print("检查文件是否存在:", os.path.exists("token.json"))
                if os.path.exists("token.json"):
                    with open("token.json", "r", encoding="utf-8") as f:
                        content = f.read()
                        print("文件内容:", content)
            else:
                print("headers为空，未找到有效的认证信息")
        except Exception as e:
            print(f"解析登录响应失败: {e}")
            import traceback
            traceback.print_exc()  # 打印详细的错误堆栈
            return None
    return None

def test_get_order_list():
    url = "https://test-tooduduapi.ptdplat.com/api/pc/member/order/index"
    try:
        # 读取保存的认证信息
        with open("token.json", "r", encoding="utf-8") as f:
            saved_data = json.load(f)

        # 从保存的数据中获取headers
        saved_headers = saved_data.get("headers", {})

        # 构建正确请求头
        request_headers = {
            'Content-Type': 'application/json'
        }
        # 从保存的headers中提取认证相关的信息
        # 常见的认证头包括：
        if 'Set-Cookie' in saved_headers:
            request_headers['Cookie'] = saved_headers['Set-Cookie']
            print(request_headers['Cookie'])

            print("已设置Cookie:", request_headers['Cookie'])
        if 'Authorization' in saved_headers:
            request_headers['Authorization'] = saved_headers['Authorization']
        if 'token' in saved_headers:
            request_headers['Authorization'] = f"Bearer {saved_headers['token']}"

            # 如果有其他自定义的认证头，也需要添加
        for key, value in saved_headers.items():
            if 'token' in key.lower() or 'auth' in key.lower():
                print(f"发现可能的认证头: {key} = {value}")
        # 使用session保持会话状态
        session = requests.Session()
        res = session.get(url, headers=request_headers)
        print(f"响应状态码: {res.status_code}")

        try:
            response_json = res.json()
            print("响应JSON:", response_json)
        except json.JSONDecodeError:
            print("响应内容:", res.text[:500])  # 显示前500个字符

    except FileNotFoundError:
        print("错误: 未找到token.json文件，请先执行登录")
    except Exception as e:
        print(f"获取订单列表失败: {e}")


def test_post_order():
    url = "https://test-tooduduapi.ptdplat.com/api/pc/member/order/done/direct"
    order_data = {
            'address_id': '4950',
            'act_type': '9',
            'goods_id': '7507',
            'goods_number': '1',
            'delivery_method': 1,
            'delivery_type': 2,
            'goods_price': 1000,
            # 'timeStamp':int(time.time())
    }

    try:
            # 读取保存的认证信息
            with open("token.json", "r", encoding="utf-8") as f:
                heders_data = json.load(f)
            # 从保存的数据中获取headers
            headers = heders_data.get("headers", {})
            requests_headers = {
                'Content-Type': 'application/json'
            }
            # 从保存的headers中提取认证相关的信息
            if 'Set-Cookie' in headers:
                requests_headers['Cookie'] = headers['Set-Cookie']
                print("已设置Cookie:", requests_headers['Cookie'])
            session = requests.Session()
            res = session.post(url, json=order_data, headers=requests_headers)
            print("响应JSON:", res.json())
    except FileNotFoundError:
        print("错误: 未找到token.json文件，请先执行登录")
    except Exception as e:
        print(f"下单失败: {e}")
        import traceback
        traceback.print_exc()

