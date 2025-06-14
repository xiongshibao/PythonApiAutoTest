# 导包
import logging

import allure
import pytest
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from api.login import LoginAPI

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建测试类
class TestLoginAPI:
    # 初始化
    uuid = None

    # 前置处理
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


    @allure.feature("登录功能")
    @allure.story("用户登录")
    @allure.description("登录成功")
    # 登录成功
    def test01_success(self):
        try:
            login_data = {
                "username": "xiongshibao",
                "password": "xiongshibao",
                "grant_type":"password",
                "client_id":"bookstore_frontend",
                "client_secret":"bookstore_secret"
            }
            response = self.login_api.login(test_data=login_data)
            # 断言响应状态码为200
            assert 200 == response.status_code
            # 断言响应数据包含'成功'
            assert 'access_token' in response.text
        except requests.exceptions.ConnectionError as e:
            pytest.fail(f"连接服务器失败: {str(e)}")
        except requests.exceptions.RequestException as e:
            pytest.fail(f"请求失败: {str(e)}")
        except Exception as e:
            pytest.fail(f"测试失败: {str(e)}")

    @allure.feature("登录功能")
    @allure.story("用户登录")
    @allure.description("登录失败（用户名为空）")
    # 登录失败（用户名为空）
    def test02_without_username(self):
        try:
            login_data = {
                "username": "xiongshibao",
                "password": "",
                "grant_type":"password",
                "client_id":"bookstore_frontend",
                "client_secret":"bookstore_secret"
            }
            response = self.login_api.login(test_data=login_data)
            logger.info(f"响应内容: {response.text}")
            logger.info(f"响应状态码: {response.status_code}")
            # 断言响应状态码
            assert 400 == response.status_code
            # 断言响应数据包含'错误'
            assert 'error' in response.text
            # 断言响应json数据中code值
            # assert 500 == response.json().get("code")
        except requests.exceptions.ConnectionError as e:
            pytest.fail(f"连接服务器失败: {str(e)}")
        except requests.exceptions.RequestException as e:
            pytest.fail(f"请求失败: {str(e)}")
        except Exception as e:
            pytest.fail(f"测试失败: {str(e)}")

    @allure.feature("登录功能")
    @allure.story("用户登录")
    @allure.description("登录失败（未注册用户）")
    # 登录失败（未注册用户）
    def test03_username_not_exist(self):
        try:
            login_data = {
                "username": "jack666",
                "password": "123456",
                "grant_type":"password",
                "client_id":"bookstore_frontend",
                "client_secret":"bookstore_secret"
            }
            response = self.login_api.login(test_data=login_data)
            logger.info(f"响应内容: {response.text}")
            logger.info(f"响应状态码: {response.status_code}")
            # 断言响应状态码为200
            assert 400 == response.status_code
            # 断言响应数据包含'错误'
            assert 'error' in response.text
            # 断言响应json数据中code值
            # assert 500 == response.json().get("code")
        except requests.exceptions.ConnectionError as e:
            pytest.fail(f"连接服务器失败: {str(e)}")
        except requests.exceptions.RequestException as e:
            pytest.fail(f"请求失败: {str(e)}")
        except Exception as e:
            pytest.fail(f"测试失败: {str(e)}")

