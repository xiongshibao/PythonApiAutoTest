# 登录：
# 地址：http://localhost:8080/oauth/token
# 方法：Get
# 请求数据：
# 请求头：Content-Type: application/json
# 请求体：username=icyfenix&password=MFfTW3uNI4eqhwDkG7HP9p2mzEUu%2Fr2&grant_type=password&client_id=bookstore_frontend&client_secret=bookstore_secret
#

# 接口封装时，重点是依据接口文档封装接口信息，需要使用的测试数据是从测试用例传递的、接口方法被调用时需要返回对应的响应结果

# 导包
import requests
import config


# 创建接口类
class LoginAPI:
    # 初始化
    def __init__(self):
        # 指定url基本信息
        # self.url_login = "http://kdtx-test.itheima.net/api/login"
        self.url_login = config.BASE_URL + "/oauth/token"
        self.headers = {
            "Content-Type": "application/json"
        }

    # 登录
    def login(self, test_data):
        params = []
        for key, value in test_data.items():
            params.append(f"{key}={value}")
        real_url = f"{self.url_login}?{'&'.join(params)}"

        return requests.get(url=real_url, headers=self.headers)

