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
    rand= random.randint(10000, 99999)
    page.locator('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[2]/i').click()
    modal = page.wait_for_selector('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[5]/div/div')
    elements = modal.query_selector_all('input[class="el-input__inner"]')
    elements[0].fill(f"lc_{random.randint(10000, 99999)}")
    elements[1].fill(f"lc_{rand}")
    elements[2].fill(f"lc_{rand}")
    time.sleep(1)
    modal.wait_for_selector('button[class="el-button el-button--primary"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info('test_update_password 修改：%s', message)


def test_update_mail():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/manage/setting')
    page.locator('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[4]/div[3]/i').click()
    modal = page.wait_for_selector('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[6]/div/div')
    modal.wait_for_selector('input[class="el-input__inner"]').fill(f"{random.randint(1000, 9999)}@qq.com")
    modal.wait_for_selector('button[class="el-button el-button--primary"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info('test_update_mail 修改邮箱：%s', message)

def test_update_phone():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/manage/setting')
    page.locator('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[6]/div[3]/i').click()
    modal = page.wait_for_selector('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[6]/div/div')
    modal.wait_for_selector('input[class="el-input__inner"]').fill(f"1851300{random.randint(1000, 9999)}")
    modal.wait_for_selector('button[class="el-button el-button--primary"]').click()
    time.sleep(2)
    # 手机号复原
    page.locator('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[6]/div[3]/i').click()
    modal = page.wait_for_selector('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[6]/div/div')
    modal.wait_for_selector('input[class="el-input__inner"]').fill(f"18513006430")
    modal.wait_for_selector('button[class="el-button el-button--primary"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info('test_update_phone 修改手机号：%s', message)


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
    log.log().info('test_copy_url 复制的登陆地址：%s', message)



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
    log.log().info('test_copy_username 复制的默认别名：%s', message)


with sync_playwright() as playwright:
    test_update_username()
    test_update_password()
    test_update_mail()
    test_update_phone()
    test_copy_url()
    test_copy_username()
