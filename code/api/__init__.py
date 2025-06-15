"""
API接口模块包
包含以下功能：
1. OMS系统接口
2. 其他系统接口
"""

from .oms.stock_age_api import StockAgeAPI
from .oms.login_api import LoginAPI

# 方式1：直接从common包导入

# 方式2：从具体模块导入

__all__ = [
    'StockAgeAPI',
    'LoginAPI'
]