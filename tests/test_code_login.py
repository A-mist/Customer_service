from playwright.sync_api import sync_playwright, Playwright
from config import browser_config,log


def test_code_login_true():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/login')
    page.locator('//*[@id="login-box"]/form/div[3]/div/div/button[1]/span').click()
    page.locator('[placeholder="请输入手机号"]').fill('18513006430')
    page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info("test_code_login_true 登陆提示: %s", message)

def test_code_login_false():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/login')
    page.locator('//*[@id="login-box"]/form/div[3]/div/div/button[1]/span').click()
    page.locator('[placeholder="请输入手机号"]').fill('18513006430')
    page.locator('[placeholder="请输入验证码"]').fill('000200')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info("test_code_login_false 登陆提示: %s", message)


def test_code_login_null():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/login')
    page.locator('//*[@id="login-box"]/form/div[3]/div/div/button[1]/span').click()
    page.locator('[placeholder="请输入手机号"]').fill('18513006430')
    # page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-form-item__error').inner_text()
    log.log().info(f"test_code_login_null 登陆提示: %s", message)


def test_code_phone_login_false():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/login')
    page.locator('//*[@id="login-box"]/form/div[3]/div/div/button[1]/span').click()
    page.locator('[placeholder="请输入手机号"]').fill('18513006130')
    page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info(f"test_code_phone_login_false 登陆提示: %s", message)


with sync_playwright() as playwright:
    log.log().info(f"----------验证码登陆 UI自动化测试---------")
    test_code_login_true()
    test_code_login_false()
    test_code_login_null()
    test_code_phone_login_false()
