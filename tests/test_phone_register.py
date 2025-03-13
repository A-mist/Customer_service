import random
from config import log,browser_config
from playwright.sync_api import sync_playwright,expect

# 注册成功
def test_phone_register_true():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('[placeholder="请输入手机号"]').fill(f"1851300{random.randint(1000,9999)}")
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('[placeholder="确认密码"]').fill('20180914l')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click()
    page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info("test_phone_register_true 登陆提示：%s", message)

#密码为空
def test_phone_register_passwordnull():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('[placeholder="请输入手机号"]').fill(f"1851300{random.randint(1000,9999)}")
    # page.locator('[placeholder="请输入密码"]').fill('20180914l')
    # page.locator('[placeholder="确认密码"]').fill('20180914l')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div[1]/div/span/span/div/span').click() # 获取验证码，测试环境可以不点击
    page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('//*[@id="login-box"]/form/div[2]/div/div[2]').inner_text()
    log.log().info("test_phone_register_passwordnull 登陆提示：%s", message)

# 两次密码不一致
def test_phone_register_passwordno():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('[placeholder="请输入手机号"]').fill(f"1851300{random.randint(1000,9999)}")
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('[placeholder="确认密码"]').fill('20180914q')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click()
    page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-form-item__error').inner_text()
    log.log().info("test_phone_register_passwordNo 登陆提示：%s", message)

# 密码不符合规则
def test_phone_register_passwordfalse():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('[placeholder="请输入手机号"]').fill(f"1851300{random.randint(1000,9999)}")
    page.locator('[placeholder="请输入密码"]').fill('2018')
    page.locator('[placeholder="确认密码"]').fill('2018')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click()
    page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('//*[@id="login-box"]/form/div[2]/div/div[2]').inner_text()
    log.log().info("test_phone_register_passwordfalse 登陆提示：%s", message)

# 验证码不正确
def test_phone_register_codefalse():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('[placeholder="请输入手机号"]').fill(f"1851300{random.randint(1000,9999)}")
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('[placeholder="确认密码"]').fill('20180914l')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click()
    page.locator('[placeholder="请输入验证码"]').fill('000100')
    page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info("test_phone_register_codefalse 登陆提示：%s", message)

# 验证码为空
def test_phone_register_codenull():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('[placeholder="请输入手机号"]').fill(f"1851300{random.randint(1000,9999)}")
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('[placeholder="确认密码"]').fill('20180914l')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click()
    # page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    messages = page.locator('.el-form-item__error').inner_text()
    log.log().info("test_phone_register_codenull 登陆提示：%s", messages)

# 手机号已注册
def test_phone_false_register():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('[placeholder="请输入手机号"]').fill(f"18513006430")
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('[placeholder="确认密码"]').fill('20180914l')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click()
    page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    messages = page.locator('.el-message__content').inner_text()
    log.log().info("test_phone_false_register 登陆提示：%s", messages)


# 手机号已注册
def test_phone_register_agreement():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('[placeholder="请输入手机号"]').fill(f"18513006430")
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('[placeholder="确认密码"]').fill('20180914l')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click()
    page.locator('[placeholder="请输入验证码"]').fill('000000')
    # page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    messages = page.locator('.el-message__content').inner_text()
    log.log().info("test_phone_register_agreement 登陆提示：%s", messages)


with sync_playwright() as playwright:
    log.log().info(f"----------手机号注册UI自动化测试---------")
    test_phone_register_true()
    test_phone_false_register()
    test_phone_register_passwordnull()
    test_phone_register_passwordfalse()
    test_phone_register_passwordno()
    test_phone_register_codefalse()
    test_phone_register_codenull()
    test_phone_register_agreement()

