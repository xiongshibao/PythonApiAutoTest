import allure
import pytest

from api.oms.stock_age_api import StockAgeAPI
from common.logger import logger


@allure.feature("OMS系统")
@allure.story("库存账龄查询模块-OpenAPI-批量测试")
class TestStockAgeOpenAPIBatch:
    """库存账龄查询测试类-OpenAPI形式-批量测试"""
    
    def setup_class(self):
        """初始化"""
        try:
            self.stock_age_api = StockAgeAPI()
            logger.info("初始化成功")
        except Exception as e:
            logger.error(f"初始化失败: {str(e)}")
            raise
    
    @pytest.mark.parametrize("test_case", [
        ("success", "WH001", "SKU001", 1, 10, 200, "data", "库存账龄查询成功"),
        ("empty_params", None, None, None, None, 200, "data", "空参数测试通过"),
        ("invalid_warehouse", "", "SKU001", 1, 10, 400, "仓库编码不能为空", "参数错误测试通过"),
        ("invalid_page_num", "WH001", "SKU001", 0, 10, 400, "页码必须大于0", "页码错误测试通过"),
        ("invalid_page_size", "WH001", "SKU001", 1, 101, 400, "每页条数必须在1-100之间", "页大小错误测试通过")
    ])
    def test_stock_age_batch(self, test_case):
        """
        批量测试库存账龄查询
        :param test_case: 测试用例数据元组
        """
        try:
            # 解包测试数据
            (test_name, warehouse_code, sku_code, page_num, 
             page_size, expected_status, expected_message, success_message) = test_case
            
            # 设置测试用例标题
            allure.dynamic.title(f"库存账龄查询-{test_name}")
            
            # 构建请求参数
            params = {}
            if warehouse_code is not None:
                params['warehouseCode'] = warehouse_code
            if sku_code is not None:
                params['skuCode'] = sku_code
            if page_num is not None:
                params['pageNum'] = page_num
            if page_size is not None:
                params['pageSize'] = page_size
            
            # 发送请求
            response = self.stock_age_api.query_stock_age(params)
            
            # 验证响应
            assert response.status_code == expected_status, \
                f"状态码不匹配: 期望 {expected_status}, 实际 {response.status_code}"
            
            if expected_message in response.text:
                if "data" in response.text:
                    response_json = response.json()
                    assert "total" in response_json["data"], "响应数据缺少total字段"
                    assert "list" in response_json["data"], "响应数据缺少list字段"
                logger.info(f"测试用例 '{test_name}' 执行成功: {success_message}")
            else:
                assert False, f"响应消息不匹配: {response.text}"
                
        except AssertionError as e:
            logger.error(f"测试用例 '{test_name}' 断言失败: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"测试用例 '{test_name}' 执行失败: {str(e)}")
            raise

# 运行说明：
# pytest test_oms_stock_age_openapi_batch.py -v