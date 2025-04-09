# 配置日志
import logging
import os
from log.config import logging_path

def setup_logger():
    # 创建日志目录
    os.makedirs(os.path.dirname(logging_path), exist_ok=True)
    
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(logging_path),  # 输出到文件
            logging.StreamHandler()  # 输出到控制台
        ]
    )
    return logging.getLogger()

# 初始化日志对象
logger = setup_logger()


def log():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(logging_path),  # 输出到文件
            logging.StreamHandler()  # 输出到控制台
        ]
    )
    return logging



def api_log():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(logging_path),  # 输出到文件
            logging.StreamHandler()  # 输出到控制台
        ]
    )
    return logging





