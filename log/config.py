import os

# 获取当前文件夹的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 构建 日志 文件的路径
logging_path = os.path.join(current_dir, "logging.txt")
