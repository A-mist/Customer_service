# 配置日志
import logging


def log():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f"/home/lilongwei/PycharmProjects/Customer_service/log/logging.txt"),  # 输出到文件
            logging.StreamHandler()  # 输出到控制台
        ]
    )

    return logging







