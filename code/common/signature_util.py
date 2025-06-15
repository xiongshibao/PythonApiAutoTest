import hashlib
import json
import time
from common.logger import logger

class SignatureUtil:
    """签名工具类"""
    
    @staticmethod
    def generate_signature(params, app_id, app_secret, timestamp):
        """
        生成签名
        :param params: 请求参数
        :param app_id: 应用ID
        :param app_secret: 应用密钥
        :param timestamp: 时间戳
        :return: 签名
        """
        try:
            # 如果参数为空，直接使用app_id、app_secret和时间戳生成签名
            if not params:
                sign_str = f"{app_id}{app_secret}{timestamp}"
            else:
                # 将参数转换为JSON字符串，确保不换行、不添加空格
                param_str = json.dumps(params, ensure_ascii=False, separators=(',', ':'))
                # 拼接app_id、app_secret、时间戳和参数
                sign_str = f"{app_id}{app_secret}{timestamp}{param_str}"
            
            logger.info(f"签名原文: {sign_str}")
            # MD5加密
            signature = hashlib.md5(sign_str.encode('utf-8')).hexdigest()
            logger.info(f"生成签名: {signature}")
            return signature
        except Exception as e:
            logger.error(f"生成签名失败: {str(e)}")
            raise
    
    @staticmethod
    def get_timestamp():
        """
        获取毫秒级时间戳
        :return: 时间戳字符串
        """
        return str(int(time.time() * 1000))
    
    @staticmethod
    def get_headers(params, app_id, app_secret):
        """
        获取请求头
        :param params: 请求参数
        :param app_id: 应用ID
        :param app_secret: 应用密钥
        :return: 请求头字典
        """
        try:
            timestamp = SignatureUtil.get_timestamp()
            signature = SignatureUtil.generate_signature(params, app_id, app_secret, timestamp)
            
            headers = {
                "Content-Type": "application/json",
                "app-id": app_id,
                "timestamp": timestamp,
                "signature": signature
            }
            logger.info(f"生成请求头: {headers}")
            return headers
        except Exception as e:
            logger.error(f"生成请求头失败: {str(e)}")
            raise 