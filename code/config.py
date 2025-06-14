# 存放被测试项目基本信息，如URL地址等

# 导包
import os

# 设置项目环境域名
BASE_URL = "http://127.0.0.1:8080/"

# 获取项目根路径
BASE_PATH = os.path.dirname(__file__)
print(BASE_PATH)
