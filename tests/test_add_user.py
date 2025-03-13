import time
import random

from playwright.sync_api  import sync_playwright
from config import browser_config, log


def test_add_user():
    page = browser_config.new_browser(playwright=playwright)
    ran = random.randint(10000,99999)
    page.goto('https://testai.ptdplat.com/manage/user')
    page.locator('button[class="el-button el-button--danger ML20"]').click()
    modal = page.wait_for_selector('div[class="el-dialog el-dialog--center preview-dialog"]')
    elements = modal.query_selector_all('input[class="el-input__inner"]')
    elements[0].fill(f'lc_{ran}')
    elements[1].fill(f'lc_{ran}')
    element = modal.query_selector_all('span[class="el-checkbox__inner"]')
    element[0].click()
    time.sleep(1)
    modal.wait_for_selector('button[class="el-button el-button--primary"]').click()
    time.sleep(5)
    moda = page.wait_for_selector('div[class="el-dialog is-align-center el-dialog--center preview-dialog"]')
    time.sleep(10)
    moda.wait_for_selector('i[class="iconfont cursor icon-fuzhi"]').click()
    message = page.locator('.el-message__content').inner_text()
    if "复制失败" in message:
        log.log().info('test_add_user 复制账号密码：%s', message)
    else:
        copy = page.evaluate(
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
        log.log().info('test_add_user 复制账号密码：%s', copy)



with sync_playwright() as playwright:
    log.log().info(f"----------添加用户 自动化测试---------")
    test_add_user()

