# 存放被测试项目基本信息，如URL地址等

# 导包
import os

class Config:
    """配置类"""
    # 项目根目录
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 基础URL
    BASE_URL = "http://localhost:8080"  # 根据实际环境修改
    # 日志配置
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s [%(levelname)8s] (%(filename)s:%(lineno)s) %(message)s"
    LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# 获取项目根路径
BASE_PATH = os.path.dirname(__file__)
print(BASE_PATH)
