import subprocess
import time
import arrow
from config import log
from pathlib import Path


folder_path =f"/home/MoTong/code/Customer_service-master/Customer_service-master/tests"


def get_filenames_using_glob(folder_path):
    folder = Path(folder_path)
    # 获取文件夹下的所有文件
    filenames = [f.name for f in folder.glob('*') if f.is_file()]
    return filenames


def run():
    for filename in get_filenames_using_glob(folder_path):
        result = subprocess.run(
            ["python", f'tests/{filename}'],
            capture_output=True,
            text=True
        )
        print(f"运行 {filename} 结果:")
        print("错误:", result.stderr)
        print("输出:", result.stdout)
        print("返回码:", result.returncode)
        print("-" * 50)


if __name__ == '__main__':
    while True:
        log.log().info(f'开始新一轮执行...当前时间：{arrow.now().format('YYYY-MM-DD HH:mm:ss')}')
        run()
        time.sleep(52200)

