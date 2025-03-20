import time
import random
from time import sleep

from playwright.sync_api  import sync_playwright
from config import browser_config, log



def tests_search_user():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/manage/user')
    modal = page.wait_for_selector('table[class="el-table__body"]')
    enumerates = modal.query_selector_all('div[class="cell"]')
    page.query_selector('input[class="el-input__inner"]').fill(enumerates[10].inner_text())
    page.wait_for_selector('button[class="el-button el-button--primary ML20"]').click()
    name = enumerates[10].inner_text()
    time.sleep(1)
    modal = page.wait_for_selector('table[class="el-table__body"]')
    enumerates = modal.query_selector_all('div[class="cell"]')
    if name == enumerates[2].inner_text():
        log.log().info('用户查询成功：%s', enumerates[1].inner_text())
    else:
        log.log().info('用户查询失败')



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
    modal.wait_for_selector('button[class="el-button el-button--primary"]').click()
    moda = page.wait_for_selector('div[class="el-dialog is-align-center el-dialog--center preview-dialog"]')
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


def tests_delete_user():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/manage/user')
    modal = page.wait_for_selector('table[class="el-table__body"]')
    modal.query_selector('span[class="fs14 co-333 cursor-p"]').click()
    modal = page.wait_for_selector('div[class="el-overlay-message-box"]')
    modal.query_selector('button[class="el-button el-button--primary"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info('tests_delete_user 删除用户：%s', message)



with sync_playwright() as playwright:
    log.log().info(f"----------用户 UI自动化测试---------")
    test_add_user()
    tests_search_user()
    tests_delete_user()
