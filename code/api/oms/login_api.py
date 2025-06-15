import requests
import allure
from common.base_api import BaseApi
from common.logger import logger

class LoginAPI(BaseApi):
    """登录接口类"""
    
    def __init__(self):
        super().__init__()
        self.login_url = "/open-sdk/oms/login"
    
    @allure.step("登录接口")
    def login(self, username, password):
        """
        登录接口
        :param username: 用户名
        :param password: 密码
        :return: 响应对象
        """
        data = {
            "username": username,
            "password": password,
            "grant_type": "password",
            "client_id": "oms_frontend",
            "client_secret": "oms_secret"
        }
        logger.info(f"登录请求参数: {data}")
        response = self.post(self.login_url, json=data)
        logger.info(f"登录响应结果: {response.text}")
        return response 