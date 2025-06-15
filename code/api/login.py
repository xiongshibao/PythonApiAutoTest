# 登录：
# 地址：http://localhost:8080/oauth/token
# 方法：Get
# 请求数据：
# 请求头：Content-Type: application/json
# 请求体：username=icyfenix&password=MFfTW3uNI4eqhwDkG7HP9p2mzEUu%2Fr2&grant_type=password&client_id=bookstore_frontend&client_secret=bookstore_secret
#

# 接口封装时，重点是依据接口文档封装接口信息，需要使用的测试数据是从测试用例传递的、接口方法被调用时需要返回对应的响应结果

# 导包
import requests
from common.base_api import BaseApi
from config import Config


# 创建接口类
class LoginAPI(BaseApi):
    # 初始化
    def __init__(self):
        super().__init__()
        # 指定url基本信息
        self.url_login = "/oauth/token"

    # 登录
    def login(self, test_data):
        """
        登录接口
        :param test_data: 登录参数
        :return: 响应对象
        """
        # 构建请求参数
        params = []
        for key, value in test_data.items():
            params.append(f"{key}={value}")
        
        # 拼接URL和参数
        url = f"{self.url_login}?{'&'.join(params)}"
        
        # 发送GET请求
        return self.get(url)

