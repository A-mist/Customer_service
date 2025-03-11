import logging
import time
import arrow
from threading import Thread
from config import log
from tests.test_phone_register import test_phone_register_true


def run_script(script_name):
    """ 封装子进程执行 """
    import subprocess
    subprocess.call(["python", f'tests/{script_name}'])

# 要运行的脚本列表
scripts = ["test_mail_login.py", "test_phone_login.py","test_code_login.py", 'test_phone_register.py']

# 创建线程列表
threads = []
for script in scripts:
    t = Thread(target=run_script, args=(script,))
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()
print("所有脚本执行完毕")

# 定时执行（每1小时运行一次）
while True:
    # 写入日志文件
    log.log().info(f"开始新一轮执行...当前时间：{arrow.now().format('YYYY-MM-DD HH:mm:ss')}" )
    for script in scripts:
        Thread(target=run_script, args=(script,)).start()
    time.sleep(36000)  # 休眠10分钟

