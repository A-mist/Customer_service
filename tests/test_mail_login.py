from playwright.sync_api import sync_playwright
from config import browser_config,log


def test_mail_login_true():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/login')
    page.locator('//*[@id="tab-email"]').click()
    page.locator('[placeholder="请输入邮箱"]').fill('1477051339@qq.com')
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info("test_mail_login_true 登陆提示: %s", message)


def test_password_false():
    page = browser_config.new_browser_nologin(playwright=playwright)

    page.goto('https://testai.ptdplat.com/login')
    page.locator('//*[@id="tab-email"]').click()
    page.locator('[placeholder="请输入邮箱"]').fill('1477051339@qq.com')
    page.locator('[placeholder="请输入密码"]').fill('20180914ll')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info("test_password_false 登陆提示: %s", message)

def test_mail_false():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/login')
    page.locator('//*[@id="tab-email"]').click()
    page.locator('[placeholder="请输入邮箱"]').fill('1477051339@qq.co')
    page.locator('[placeholder="请输入密码"]').fill('20180914ll')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text(timeout=3000)
    log.log().info("test_mail_false 登陆提示: %s", message)

def test_mail_null():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/login')
    page.locator('//*[@id="tab-email"]').click()
    # page.locator('[placeholder="请输入邮箱"]').fill('18513006411')
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-form-item__error').inner_text(timeout=3000)
    log.log().info("test_mail_null 登陆提示: %s", message)

def test_password_null():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/login')
    page.locator('//*[@id="tab-email"]').click()
    page.locator('[placeholder="请输入邮箱"]').fill('1477051339@qq.com')
    # page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-form-item__error').inner_text(timeout=3000)
    log.log().info("test_password_null 登陆提示: %s", message)

with sync_playwright() as playwright:
    log.log().info(f"----------邮箱登陆 UI自动化测试---------")
    test_mail_login_true()
    test_mail_false()
    test_password_false()
    test_mail_null()
    test_password_null()
