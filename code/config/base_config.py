"""
基础配置模块
包含系统基础配置信息
"""

class Config:
    """基础配置类"""
    
    # 基础URL配置
    BASE_URL = "http://localhost:8080"  # 请根据实际环境修改
    
    # 其他基础配置
    TIMEOUT = 30  # 请求超时时间（秒）
    MAX_RETRIES = 3  # 最大重试次数
    
    # 日志配置
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s" 