import random
from playwright.sync_api import sync_playwright
from config import log,browser_config


#注册成功
def test_mail_register_true():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('//*[@id="tab-email"]').click()
    page.locator('[placeholder="请输入邮箱"]').fill(f"14770{random.randint(10000,99999)}@qq.com")
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('[placeholder="确认密码"]').fill('20180914l')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click() # 发送验证码，测试环境可以不点击
    page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info("test_mail_register_true 登陆提示：%s", message)


# 邮箱错误
def test_mail_false_register():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('//*[@id="tab-email"]').click()
    page.locator('[placeholder="请输入邮箱"]').fill(f"14770{random.randint(10000,99999)}")
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('[placeholder="确认密码"]').fill('20180914l')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click() # 发送验证码，测试环境可以不点击
    page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-form-item__error').inner_text()
    log.log().info("test_mail_register_true 登陆提示：%s", message)

# 邮箱已注册
def test_mail_registered():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('//*[@id="tab-email"]').click()
    page.locator('[placeholder="请输入邮箱"]').fill(f"1477051339@qq.com")
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('[placeholder="确认密码"]').fill('20180914l')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click() # 发送验证码，测试环境可以不点击
    page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info("test_mail_register_true 登陆提示：%s", message)


# 邮箱为空
def test_mail_null_register():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('//*[@id="tab-email"]').click()
    # page.locator('[placeholder="请输入邮箱"]').fill(f"14770{random.randint(10000,99999)}@qq.com")
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('[placeholder="确认密码"]').fill('20180914l')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click() # 发送验证码，测试环境可以不点击
    page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-form-item__error').inner_text()
    log.log().info("test_mail_register_true 登陆提示：%s", message)


# 密码规则错误
def test_mail_register_passwordfalse():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('//*[@id="tab-email"]').click()
    page.locator('[placeholder="请输入邮箱"]').fill(f"14770{random.randint(10000,99999)}@qq.com")
    page.locator('[placeholder="请输入密码"]').fill('20180914')
    page.locator('[placeholder="确认密码"]').fill('20180914')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click() # 发送验证码，测试环境可以不点击
    page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-form-item__error').inner_text()
    log.log().info("test_mail_register_passwordfalse 登陆提示：%s", message)


# 密码为空
def test_mail_register_passwordnull():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('//*[@id="tab-email"]').click()
    page.locator('[placeholder="请输入邮箱"]').fill(f"14770{random.randint(10000,99999)}@qq.com")
    # page.locator('[placeholder="请输入密码"]').fill('20180914l')
    # page.locator('[placeholder="确认密码"]').fill('20180914l')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click() # 发送验证码，测试环境可以不点击
    page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('//*[@id="login-box"]/form/div[2]/div/div[2]').inner_text()
    log.log().info("test_mail_register_passwordnull 登陆提示：%s", message)


# 两次密码不一致
def test_mail_register_passwordno():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('//*[@id="tab-email"]').click()
    page.locator('[placeholder="请输入邮箱"]').fill(f"14770{random.randint(10000,99999)}@qq.com")
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('[placeholder="确认密码"]').fill('20180914')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click() # 发送验证码，测试环境可以不点击
    page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-form-item__error').inner_text()
    log.log().info("test_mail_register_passwordno 登陆提示：%s", message)


# 验证码为空
def test_mail_register_codenull():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('//*[@id="tab-email"]').click()
    page.locator('[placeholder="请输入邮箱"]').fill(f"14770{random.randint(10000,99999)}@qq.com")
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('[placeholder="确认密码"]').fill('20180914l')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click() # 发送验证码，测试环境可以不点击
    # page.locator('[placeholder="请输入验证码"]').fill('000000')
    page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-form-item__error').inner_text()
    log.log().info("test_mail_register_codenull 登陆提示：%s", message)


# 验证码错误
def test_mail_register_code_false():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('//*[@id="tab-email"]').click()
    page.locator('[placeholder="请输入邮箱"]').fill(f"14770{random.randint(10000,99999)}@qq.com")
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('[placeholder="确认密码"]').fill('20180914l')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click() # 发送验证码，测试环境可以不点击
    page.locator('[placeholder="请输入验证码"]').fill('010000')
    page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info("test_mail_register_code_false 登陆提示：%s", message)


# 未勾选协议
def test_mail_register_agreement():
    page = browser_config.new_browser_nologin(playwright=playwright)
    page.goto('https://testai.ptdplat.com/register')
    page.locator('//*[@id="tab-email"]').click()
    page.locator('[placeholder="请输入邮箱"]').fill(f"14770{random.randint(10000,99999)}@qq.com")
    page.locator('[placeholder="请输入密码"]').fill('20180914l')
    page.locator('[placeholder="确认密码"]').fill('20180914l')
    # page.locator('//*[@id="login-box"]/form/div[4]/div/div/div/span/span/div/span').click() # 发送验证码，测试环境可以不点击
    page.locator('[placeholder="请输入验证码"]').fill('010000')
    # page.locator('.el-checkbox__inner').click()
    page.locator('//*[@id="captcha"]').click()
    message = page.locator('.el-message__content').inner_text()
    log.log().info("test_mail_register_agreement 登陆提示：%s", message)





with sync_playwright() as playwright:
    log.log().info(f"----------邮箱注册UI自动化测试---------")
    test_mail_register_true()
    test_mail_false_register()
    test_mail_null_register()
    test_mail_registered()
    test_mail_register_passwordno()
    test_mail_register_passwordnull()
    test_mail_register_passwordfalse()
    test_mail_register_codenull()
    test_mail_register_code_false()
    test_mail_register_agreement()


