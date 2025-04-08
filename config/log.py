# 配置日志
import logging
import log.config as path


def log():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(path.logging_path),  # 输出到文件
            logging.StreamHandler()  # 输出到控制台
        ]
    )
    return logging



def api_log():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(path.logging_path),  # 输出到文件
            logging.StreamHandler()  # 输出到控制台
        ]
    )
    return logging





