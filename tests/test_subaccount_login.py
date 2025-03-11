import time

from playwright.sync_api import sync_playwright
from config import log,browser_config


## 子账号登陆
# 成功登陆
def test_subaccount_login():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/login/account')
    page.locator('[placeholder="登录名 @ 别名"]').fill('test_a@737917054421567586')
    page.locator('[placeholder="请输入密码"]').fill('8-E1t%n3.i2f!GEGXknQx{KuOA')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info('test_subaccount_login 登陆提示：%s', message)

# 密码错误
def test_subaccount_password_false():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/login/account')
    page.locator('[placeholder="登录名 @ 别名"]').fill('test_a@737917054421567586')
    page.locator('[placeholder="请输入密码"]').fill('8-E1t%n3.i2fQx{KuOA')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info('test_subaccount_password_false 登陆提示：%s', message)

#  账号错误
def test_subaccount_false():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/login/account')
    page.locator('[placeholder="登录名 @ 别名"]').fill('test_a@737921567586')
    page.locator('[placeholder="请输入密码"]').fill('8-E1t%n3.i2f!GEGXknQx{KuOA')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info('test_subaccount_false 登陆提示：%s', message)



with sync_playwright() as playwright:
    log.log().info('----------子账号登陆 UI自动化测试---------')
    test_subaccount_login()
    test_subaccount_password_false()
    test_subaccount_false()
