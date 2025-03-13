from lib2to3.fixes.fix_input import context
import json
import pymysql
from playwright.sync_api import Playwright,sync_playwright,expect

# def test_delete_mysql():
#     conn = pymysql.connect(
#         host='39.107.99.174',
#         user='root',
#         password='dd_mysql',
#         database='test_ai'
#     )
#     # 创建数据库游标对象
#     cursor = conn.cursor()
#     cursor.execute("SELECT phone, password FROM users ;")
#     result = cursor.fetchall()
#     print('\n'*2+'='*20+f"\n符合条件的数据有：{len(result)} 条")
#     # 执行sql自动化数据
#     # cursor.execute("delete FROM project_tasks WHERE subject LIKE '流水线%';")
#     conn.commit()
#     print(result)
#     print(f"已删除：{len(result)} 条自动化数据\n"+'='*20)

def get_login_json():
    with open("/home/lilongwei/PycharmProjects/Customer_service/config/login.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data




def new_browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, channel="chrome")
    contexts = browser.new_context(
        viewport={
        'width': 1920,
        'height': 1080,
        },
        storage_state=get_login_json(),
        permissions=["clipboard-read"]
    )
    page = contexts.new_page()
    return page

def new_browser_nologin(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, channel="chrome")
    contexts = browser.new_context(
        viewport={
        'width': 1920,
        'height': 1080,
        },
        permissions=["clipboard-read"]
    )
    page = contexts.new_page()
    return page
