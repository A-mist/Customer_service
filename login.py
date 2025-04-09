import time

from playwright.sync_api import sync_playwright
from config import browser_config, log


def run():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/login')
    page.locator('//*[@id="login-box"]/form/div[3]/div/div/button[1]/span').click()
    page.locator('[placeholder="请输入手机号"]').fill('18513006430')
    page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.setup_logger().info("登陆提示: %s", message)
    page.context.storage_state(path='config/login.json')
    page.close()


with sync_playwright() as playwright:
    run()