import allure

from api.oms.stock_age_api import StockAgeAPI
from common.logger import logger


@allure.feature("OMS系统")
@allure.story("库存账龄查询模块-OpenAPI")
class TestStockAgeOpenAPI:
    """库存账龄查询测试类-OpenAPI形式"""
    
    def setup_class(self):
        """初始化"""
        try:
            self.stock_age_api = StockAgeAPI()
            logger.info("初始化成功")
        except Exception as e:
            logger.error(f"初始化失败: {str(e)}")
            raise
    
    @allure.title("库存账龄查询成功-OpenAPI")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_query_stock_age_success(self):
        """测试库存账龄查询成功-OpenAPI形式"""
        try:
            # 发送请求
            response = self.stock_age_api.query_stock_age({
                "warehouseCode": "WH001",
                "skuCode": "SKU001",
                "pageNum": 1,
                "pageSize": 10
            })
            
            # 验证响应
            assert response.status_code == 200, \
                f"状态码不匹配: 期望 200, 实际 {response.status_code}"
            
            response_json = response.json()
            assert "data" in response_json, "响应数据缺少data字段"
            assert "total" in response_json["data"], "响应数据缺少total字段"
            assert "list" in response_json["data"], "响应数据缺少list字段"
            
            logger.info("库存账龄查询成功")
        except AssertionError as e:
            logger.error(f"断言失败: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"测试执行失败: {str(e)}")
            raise
        
    @allure.title("库存账龄查询-空参数-OpenAPI")
    @allure.severity(allure.severity_level.NORMAL)
    def test_query_stock_age_empty_params(self):
        """测试库存账龄查询-空参数-OpenAPI形式"""
        try:
            # 发送请求
            response = self.stock_age_api.query_stock_age({})
            
            # 验证响应
            assert response.status_code == 200, \
                f"状态码不匹配: 期望 200, 实际 {response.status_code}"
            
            response_json = response.json()
            assert "data" in response_json, "响应数据缺少data字段"
            assert "total" in response_json["data"], "响应数据缺少total字段"
            assert "list" in response_json["data"], "响应数据缺少list字段"
            
            logger.info("空参数测试通过")
        except AssertionError as e:
            logger.error(f"断言失败: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"测试执行失败: {str(e)}")
            raise
        
    @allure.title("库存账龄查询-参数错误-OpenAPI")
    @allure.severity(allure.severity_level.NORMAL)
    def test_query_stock_age_invalid_params(self):
        """测试库存账龄查询-参数错误-OpenAPI形式"""
        try:
            # 发送请求
            response = self.stock_age_api.query_stock_age({
                "warehouseCode": "",  # 仓库编码为空
                "pageNum": 1,
                "pageSize": 10
            })
            
            # 验证响应
            assert response.status_code == 400, \
                f"状态码不匹配: 期望 400, 实际 {response.status_code}"
            assert "仓库编码不能为空" in response.text, \
                f"响应消息不匹配: {response.text}"
            
            logger.info("参数错误测试通过")
        except AssertionError as e:
            logger.error(f"断言失败: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"测试执行失败: {str(e)}")
            raise

# 运行说明：
# pytest test_oms_stock_age_openapi.py -v 