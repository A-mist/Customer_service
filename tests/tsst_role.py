import time
import random
from playwright.sync_api import sync_playwright
from config import browser_config,log


def test_add_role():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/manage/roleList')
    ran = random.randint(100,999)
    page.locator('button[class="el-button el-button--danger ML20"]').click()
    modal = page.wait_for_selector('div[class="el-dialog el-dialog--center preview-dialog"]')
    enumerates = modal.query_selector_all('input[class="el-input__inner"]')
    enumerates[0].fill(f'root{ran}')
    enumerates[1].fill(f'root{ran}')
    enumerates = modal.query_selector_all('span[class="el-checkbox__inner"]')
    enumerates[0].click()
    modal.query_selector('button[class="el-button el-button--primary"]').click()
    messages = page.locator('.el-message__content').inner_text()
    log.log().info(f"test_add_role 添加角色：%s %s",f'root{ran}', messages)



def test_views_role():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/manage/roleList')
    page.wait_for_selector('button[class="el-button el-button--primary is-text fs14 cursor-p"]').click()
    modal = page.wait_for_selector('div[class="el-dialog el-dialog--center preview-dialog"]')
    enumerates = modal.query_selector_all('input[class="el-input__inner"]')
    li = []
    for enumerate in enumerates:
        li.append(enumerate.input_value())
    modal.query_selector('button[class="el-button el-button--primary"]').click()
    log.log().info('test_views_role 查看角色: %s', li)



def test_update_role():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/manage/roleList')
    ran = random.randint(100, 999)
    page.wait_for_selector('button[class="el-button el-button--success is-text fs14 cursor-p"]').click()
    modal = page.wait_for_selector('div[class="el-dialog el-dialog--center preview-dialog"]')
    li = []
    enumerates = modal.query_selector_all('input[class="el-input__inner"]')
    for enumerate in enumerates:
        li.append(enumerate.input_value())
    modal.query_selector('input[class="el-input__inner"]').fill(f'root{ran}')
    modal.query_selector('button[class="el-button el-button--primary"]').click()
    massage = page.locator('.el-message__content').inner_text()
    log.log().info(f'test_update_role 修改角色：%s 修改后角色名：root{ran}，原角色名：%s', massage, li[0])

def test_delete_role():
    page = browser_config.new_browser(playwright=playwright)
    page.goto('https://testai.ptdplat.com/manage/roleList')
    page.wait_for_selector('button[class="el-button el-button--danger is-text fs14 cursor-p"]').click()
    modal = page.wait_for_selector('div[class="el-message-box el-message-box--center"]')
    modal.query_selector('button[class="el-button el-button--primary"]').click()
    massage = page.locator('.el-message__content').inner_text()
    log.log().info('test_delete_role 删除角色：%s', massage)



with sync_playwright() as playwright:
    log.log().info(f"----------添加查看修改编辑角色 自动化测试---------")
    test_add_role()
    test_views_role()
    test_update_role()
    test_delete_role()