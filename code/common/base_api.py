import requests
from common.logger import logger
from config import Config

class BaseApi:
    """基础API类"""
    
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = {
            "Content-Type": "application/json"
        }
        self.session = requests.Session()
    
    def get(self, url, params=None, **kwargs):
        """
        发送GET请求
        :param url: 请求地址
        :param params: 请求参数
        :param kwargs: 其他参数
        :return: 响应对象
        """
        url = self.base_url + url
        logger.info("="*50)
        logger.info("发送GET请求")
        logger.info(f"请求地址: {url}")
        logger.info(f"请求头: {self.headers}")
        if params:
            logger.info(f"请求参数: {params}")
        if kwargs:
            logger.info(f"其他参数: {kwargs}")
            
        response = self.session.get(url, params=params, headers=self.headers, **kwargs)
        
        logger.info("="*50)
        logger.info("收到响应")
        logger.info(f"响应状态码: {response.status_code}")
        logger.info(f"响应头: {dict(response.headers)}")
        logger.info(f"响应内容: {response.text}")
        logger.info("="*50)
        
        return response
    
    def post(self, url, data=None, json=None, **kwargs):
        """
        发送POST请求
        :param url: 请求地址
        :param data: 表单数据
        :param json: JSON数据
        :param kwargs: 其他参数
        :return: 响应对象
        """
        url = self.base_url + url
        logger.info("="*50)
        logger.info("发送POST请求")
        logger.info(f"请求地址: {url}")
        logger.info(f"请求头: {self.headers}")
        if data:
            logger.info(f"表单数据: {data}")
        if json:
            logger.info(f"JSON数据: {json}")
        if kwargs:
            logger.info(f"其他参数: {kwargs}")
            
        response = self.session.post(url, data=data, json=json, headers=self.headers, **kwargs)
        
        logger.info("="*50)
        logger.info("收到响应")
        logger.info(f"响应状态码: {response.status_code}")
        logger.info(f"响应头: {dict(response.headers)}")
        logger.info(f"响应内容: {response.text}")
        logger.info("="*50)
        
        return response 