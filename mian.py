import subprocess
import time
import arrow
from config import log


scripts = [
            "test_mail_login.py",
            "test_phone_login.py",
            "test_code_login.py",
            'test_phone_register.py',
            'test_mail_register.py',
            'test_subaccount_login.py',
           ]


def run():
    for script in scripts:
        result = subprocess.run(
            ["python", f'tests/{script}'],
            capture_output=True,
            text=True
        )
        print(f"运行 {script} 结果:")
        print("错误:", result.stderr)
        print("输出:", result.stdout)
        print("返回码:", result.returncode)
        print("-" * 40)


if __name__ == '__main__':
    while True:
        log.log().info(f'开始新一轮执行...当前时间：{arrow.now().format('YYYY-MM-DD HH:mm:ss')}')
        run()
        time.sleep(52200)

