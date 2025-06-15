import time
import random
import allure
from locust import HttpUser, task, between
from common.logger import logger
from config.openapi_config import OpenAPIConfig

class LoginLoadTest(HttpUser):
    """登录接口压力测试类"""
    
    # 设置请求间隔时间（秒）
    wait_time = between(1, 3)
    
    def on_start(self):
        """测试开始前的准备工作"""
        logger.info("开始登录接口压力测试")
    
    @task(3)  # 权重为3，表示这个测试用例的执行频率更高
    def test_login_success(self):
        """测试正常登录场景"""
        try:
            # 发送请求
            with self.client.post(
                "/oauth/token",
                json={
                    "username": "admin",
                    "password": "123456"
                },
                catch_response=True
            ) as response:
                if response.status_code == 200 and "token" in response.text:
                    response.success()
                    logger.info("正常登录测试通过")
                else:
                    response.failure(f"登录失败: {response.text}")
                    logger.error(f"登录失败: {response.text}")
        except Exception as e:
            logger.error(f"测试执行异常: {str(e)}")
    
    @task(1)
    def test_login_invalid_password(self):
        """测试密码错误场景"""
        try:
            with self.client.post(
                "/oauth/token",
                json={
                    "username": "admin",
                    "password": "wrong_password"
                },
                catch_response=True
            ) as response:
                if response.status_code == 401 and "密码错误" in response.text:
                    response.success()
                    logger.info("密码错误测试通过")
                else:
                    response.failure(f"测试失败: {response.text}")
                    logger.error(f"测试失败: {response.text}")
        except Exception as e:
            logger.error(f"测试执行异常: {str(e)}")
    
    @task(1)
    def test_login_empty_username(self):
        """测试用户名为空场景"""
        try:
            with self.client.post(
                "/oauth/token",
                json={
                    "username": "",
                    "password": "123456"
                },
                catch_response=True
            ) as response:
                if response.status_code == 400 and "用户名不能为空" in response.text:
                    response.success()
                    logger.info("用户名为空测试通过")
                else:
                    response.failure(f"测试失败: {response.text}")
                    logger.error(f"测试失败: {response.text}")
        except Exception as e:
            logger.error(f"测试执行异常: {str(e)}")
    
    @task(1)
    def test_login_empty_password(self):
        """测试密码为空场景"""
        try:
            with self.client.post(
                "/oauth/token",
                json={
                    "username": "admin",
                    "password": ""
                },
                catch_response=True
            ) as response:
                if response.status_code == 400 and "密码不能为空" in response.text:
                    response.success()
                    logger.success()
                    logger.info("密码为空测试通过")
                else:
                    response.failure(f"测试失败: {response.text}")
                    logger.error(f"测试失败: {response.text}")
        except Exception as e:
            logger.error(f"测试执行异常: {str(e)}")
    
    def on_stop(self):
        """测试结束后的清理工作"""
        logger.info("登录接口压力测试结束")

# 运行说明：
# 1. 安装locust: pip install locust
# 2. 在命令行中运行: locust -f test_oms_login_load.py
# 3. 打开浏览器访问: http://localhost:8089
# 4. 设置以下参数：
#    - Number of users: 要模拟的并发用户数
#    - Spawn rate: 每秒启动的用户数
#    - Host: 被测系统的URL（例如：http://localhost:8080）
# 5. 点击"Start swarming"开始测试 