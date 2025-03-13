import logging
import time
from pathlib import Path
from threading import Thread

import arrow
from config import log


def run_script(script_name):
    """ 封装子进程执行 """
    import subprocess
    subprocess.call(["python", f'tests/{script_name}'])

folder_path =f"/home/lilongwei/PycharmProjects/Customer_service/tests"

def get_filenames_using_glob(folder_path):
    folder = Path(folder_path)
    # 获取文件夹下的所有文件
    filenames = [f.name for f in folder.glob('*') if f.is_file()]
    return filenames

# 创建线程列表
threads = []
for script in get_filenames_using_glob(folder_path):
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
    for script in  get_filenames_using_glob(folder_path):
        Thread(target=run_script, args=(script,)).start()
    time.sleep(36000)  # 休眠10分钟

