# 导包
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry
from api.login import LoginAPI
import pytest
import json
import config

# 读取json文件
def build_data(json_file):
    # 定义空列表
    test_data = []
    # 打开json文件，指定编码为utf-8
    with open(json_file, "r", encoding='utf-8') as f:
        # 加载json文件数据
        json_data = json.load(f)
        # 循环遍历测试数据
        for case_data in json_data:
            # 转换数据格式[{},{}] ==> [(),()]
            username = case_data.get("username")
            password = case_data.get("password")
            status = case_data.get("status")
            message = case_data.get("message")
            test_data.append((username, password, status, message))
    # 返回处理之后测试数据
    return test_data

# 创建测试类
class TestLoginAPI:
    # 初始化
    uuid = None

    @pytest.fixture(autouse=True)
    def setup(self):
        # 实例化接口类
        self.login_api = LoginAPI()
        # 设置重试策略
        self.session = requests.Session()
        retry = Retry(
            total=3,  # 总重试次数
            backoff_factor=0.5,  # 重试间隔
            status_forcelist=[500, 502, 503, 504]  # 需要重试的HTTP状态码
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)

    # 后置处理
    def teardown(self):
        pass

    # 登录成功
    @pytest.mark.parametrize("username, password, status, error",
                           build_data(json_file=config.BASE_PATH + "/data/login.json"))
    def test01_success(self, username, password, status, error):
        login_data = {
            "username": username,
            "password": password,
            "grant_type": "password",
            "client_id": "bookstore_frontend",
            "client_secret": "bookstore_secret"
        }
        response = self.login_api.login(test_data=login_data)
        # 断言响应状态码为200
        assert status == response.status_code
        # 断言响应数据包含'成功'
        assert error in response.text