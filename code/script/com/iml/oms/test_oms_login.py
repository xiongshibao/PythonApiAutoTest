
import allure
from api.oms.login_api import LoginAPI

@allure.feature("OMS系统")
@allure.story("登录模块")
class TestLogin:
    """登录测试类"""
    
    def setup_class(self):
        """初始化"""
        self.login_api = LoginAPI()
    
    @allure.title("登录成功")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_success(self):
        """测试登录成功"""
        # 测试数据
        username = "admin"
        password = "123456"
        
        # 发送请求
        response = self.login_api.login(username, password)
        
        # 断言
        assert response.status_code == 200
        assert "access_token" in response.json()
        
    @allure.title("登录失败-用户名错误")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_wrong_username(self):
        """测试登录失败-用户名错误"""
        # 测试数据
        username = "wrong_user"
        password = "123456"
        
        # 发送请求
        response = self.login_api.login(username, password)
        
        # 断言
        assert response.status_code == 401
        assert "用户名或密码错误" in response.text 