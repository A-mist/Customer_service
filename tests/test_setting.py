import time
import random

from config import log,browser_config
from playwright.sync_api import sync_playwright



def test_update_username():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/manage/setting')
    page.locator('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[1]/div[3]/i').click()
    modal = page.wait_for_selector('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[3]/div/div')
    modal.wait_for_selector('input[class="el-input__inner"]').fill(f"lc_{random.randint(1000, 9999)}")
    modal.wait_for_selector('button[class="el-button el-button--primary"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info('test_update_username 修改：%s', message)


def test_update_password():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/manage/setting')
    page.locator('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[2]/i').click()
    modal = page.wait_for_selector('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[5]/div/div')
    modal.wait_for_selector('input[class="el-input__inner"]').fill(f"lc_{random.randint(1000, 9999)}")

    time.sleep(3)
    # modal.wait_for_selector('button[class="el-button el-button--primary"]').click()
    # message = page.locator('.el-message__content').inner_text()
    # log.log().info('test_update_password 修改：%s', message)


def test_update_mail():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/manage/setting')
    page.locator('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[4]/div[3]/i').click()

    modal = page.wait_for_selector('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[6]/div/div')
    modal.wait_for_selector('input[class="el-input__inner"]').fill(f"{random.randint(1000, 9999)}@qq.com")
    modal.wait_for_selector('button[class="el-button el-button--primary"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info('test_update_mail 修改：%s', message)

def test_update_phone():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/manage/setting')
    page.locator('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[6]/div[3]/i').click()
    modal = page.wait_for_selector('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[3]/div/div')
    modal.wait_for_selector('input[class="el-input__inner"]').fill(f"lc_{random.randint(1000, 9999)}")
    modal.wait_for_selector('button[class="el-button el-button--primary"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info('test_update_phone 修改：%s', message)


def test_copy_url():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/manage/setting')
    page.locator('div[class="cursor login-url"]').click()
    message = page.evaluate(
        """
            async () => {
                try 
                {
                    return await navigator.clipboard.readText();
                } 
                catch (err) 
                {
                    console.error("无法读取剪贴板:", err);
                    return null;
                }
            }
        """
                            )
    log.log().info('test_copy_url 复制的内容：%s', message)



def test_copy_username():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/manage/setting')
    time.sleep(1)
    page.locator('i[class="iconfont cursor icon-fuzhi web-copy"]').click()
    message = page.evaluate(
        """
            async () => {
                try 
                {
                    return await navigator.clipboard.readText();
                } 
                catch (err) 
                {
                    console.error("无法读取剪贴板:", err);
                    return null;
                }
            }
        """
                            )
    log.log().info('test_copy_url 复制的内容：%s', message)





with sync_playwright() as playwright:
    # test_update_username()
    test_update_password()
    # test_update_mail()
    # test_copy_url()
    # test_copy_username()
