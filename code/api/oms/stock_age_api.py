import allure
from common.base_api import BaseApi
from common.logger import logger
from common.signature_util import SignatureUtil
from config.openapi_config import OpenAPIConfig

class StockAgeAPI(BaseApi):
    """库存账龄查询接口类"""
    
    def __init__(self):
        super().__init__()
        self.stock_age_url = OpenAPIConfig.Path.STOCK_AGE_QUERY
    
    @allure.step("库存账龄查询接口")
    def query_stock_age(self, params):
        """
        库存账龄查询接口
        :param params: 查询参数
        :return: 响应对象
        """
        try:
            logger.info(f"库存账龄查询请求参数: {params}")
            # 设置请求头
            self.headers = SignatureUtil.get_headers(
                params=params,
                app_id=OpenAPIConfig.APP_ID,
                app_secret=OpenAPIConfig.APP_SECRET
            )
            # 发送请求
            response = self.get(self.stock_age_url, params=params)
            logger.info(f"库存账龄查询响应结果: {response.text}")
            return response
        except Exception as e:
            logger.error(f"库存账龄查询失败: {str(e)}")
            raise 