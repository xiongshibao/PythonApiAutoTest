"""
配置模块包
包含以下功能：
1. 基础配置
2. OpenAPI配置
3. 其他系统配置
"""

from .openapi_config import OpenAPIConfig
from .base_config import Config

__all__ = [
    'OpenAPIConfig',
    'Config'
] 