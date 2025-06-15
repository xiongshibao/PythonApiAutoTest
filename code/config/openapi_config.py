class OpenAPIConfig:
    """OpenAPI配置类"""
    
    # 应用ID
    APP_ID = "your_app_id"  # 替换为实际的app_id
    
    # 应用密钥
    APP_SECRET = "your_app_secret"  # 替换为实际的app_secret
    
    # 接口基础URL
    BASE_URL = "http://localhost:8080"  # 根据实际环境修改
    
    # 接口路径
    class Path:
        # 库存账龄查询接口
        STOCK_AGE_QUERY = "/open-sdk/oms/stock_age_query" 