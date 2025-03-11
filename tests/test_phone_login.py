from playwright.sync_api import  sync_playwright
from config import browser_config,log


def test_phone_login_true():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/login')
    page.locator('[placeholder="请输入手机号"]').fill('18513006430')
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info("test_phone_login_true 登陆提示: %s", message)

def test_password_false():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/login')
    page.locator('[placeholder="请输入手机号"]').fill('18513006430')
    page.locator('[placeholder="请输入密码"]').fill('20180914ll')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info("test_password_false 登陆提示: %s", message)


def test_phone_false():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/login')
    page.locator('[placeholder="请输入手机号"]').fill('18513006411')
    page.locator('[placeholder="请输入密码"]').fill('20180914ll')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info("test_phone_false 登陆提示: %s", message)

def test_phone_null():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/login')
    # page.locator('[placeholder="请输入手机号"]').fill('18513006411')
    page.locator('[placeholder="请输入密码"]').fill('20180914ll')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-form-item__error').inner_text()
    log.log().info("test_phone_null 登陆提示: %s", message)

def test_password_null():
    page = browser_config.new_browser(playwright=playwright)

    page.goto('https://testai.ptdplat.com/login')
    page.locator('[placeholder="请输入手机号"]').fill('18513006411')
    # page.locator('[placeholder="请输入密码"]').fill('20180914ll')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-form-item__error').inner_text()
    log.log().info("test_password_null 登陆提示: %s", message)

with sync_playwright() as playwright:
    log.log().info(f"----------手机号登陆UI自动化测试---------")
    test_phone_login_true()
    test_phone_false()
    test_password_false()
    test_phone_null()
    test_password_null()
