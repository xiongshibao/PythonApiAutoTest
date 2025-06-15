# 导包
import hashlib

import allure
import bcrypt
import pytest
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from api.login import LoginAPI
from common.logger import logger

# 创建测试类
class TestLoginAPI:
    # 初始化
    uuid = None
    CLIENT_SALT = "$2a$10$o5L.dWYEjZjaejOmN3x4Qu"

    def default_encode(self, source):
        """
        默认编码
        采用MD5加密，HEX编码，加盐，Bcrypt加密，返回
        """
        # MD5加密并转为HEX
        md5_hash = hashlib.md5(source.encode('utf-8')).hexdigest()
        # Bcrypt加密
        hashed = bcrypt.hashpw(md5_hash.encode('utf-8'), self.CLIENT_SALT.encode('utf-8'))
        # 截取掉盐值长度
        return hashed.decode('utf-8')[len(self.CLIENT_SALT):]

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
            password = "xiongshibao"
            # 使用默认编码方式加密密码
            hashed_password = self.default_encode(password)

            login_data = {
                "username": "xiongshibao",
                "password": hashed_password,
                "grant_type": "password",
                "client_id": "bookstore_frontend",
                "client_secret": "bookstore_secret"
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
            password = ""
            # 使用默认编码方式加密密码
            hashed_password = self.default_encode(password)
            logger.info(f"加密结果: {hashed_password}")

            login_data = {
                "username": "xiongshibao",
                "password": password,
                "grant_type": "password",
                "client_id": "bookstore_frontend",
                "client_secret": "bookstore_secret"
            }
            response = self.login_api.login(test_data=login_data)
            logger.info(f"响应内容: {response.text}")
            logger.info(f"响应状态码: {response.status_code}")
            # 断言响应状态码
            assert 400 == response.status_code
            # 断言响应数据包含'错误'
            assert 'error' in response.text
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
            password = "123456"
            # 使用默认编码方式加密密码
            hashed_password = self.default_encode(password)
            logger.info(f"加密结果: {hashed_password}")

            login_data = {
                "username": "jack666",
                "password": password,
                "grant_type": "password",
                "client_id": "bookstore_frontend",
                "client_secret": "bookstore_secret"
            }
            response = self.login_api.login(test_data=login_data)
            logger.info(f"响应内容: {response.text}")
            logger.info(f"响应状态码: {response.status_code}")
            # 断言响应状态码为200
            assert 400 == response.status_code
            # 断言响应数据包含'错误'
            assert 'error' in response.text
        except requests.exceptions.ConnectionError as e:
            pytest.fail(f"连接服务器失败: {str(e)}")
        except requests.exceptions.RequestException as e:
            pytest.fail(f"请求失败: {str(e)}")
        except Exception as e:
            pytest.fail(f"测试失败: {str(e)}")

