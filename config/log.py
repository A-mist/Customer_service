# 配置日志
import logging


def log():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f"/home/MoTong/code/Customer_service-master/Customer_service-master/log/logging.txt"),  # 输出到文件
            logging.StreamHandler()  # 输出到控制台
        ]
    )

    return logging



def api_log():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f"/home/MoTong/code/Customer_service-master/Customer_service-master/log/apilog.txt"),  # 输出到文件
            logging.StreamHandler()  # 输出到控制台
        ]
    )
    return logging






