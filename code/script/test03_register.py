# 需求：登录成功

# 导包
import requests
import bcrypt  # 添加bcrypt包

# 发送请求
base_url = "http://localhost:8080/restful/accounts/"
header_data = {
    "Content-Type": "application/json"
}

# 原始密码
password = "xiongshibao"
# 使用bcrypt加密密码
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# 将加密后的密码转换为字符串
hashed_password_str = hashed_password.decode('utf-8')

register_data = {
    "username": "xiongshibao",
    "password": hashed_password_str,  # 使用加密后的密码
    "name": "xiongshibao",
    "telephone": "18990000000",
    "email": "xiongshibao0000@163.com"
}

response = requests.post(url=base_url, headers=header_data, json=register_data)

# 查看响应
print("\n响应状态码：")
print(response.status_code)
print("\n响应内容：")
print(response.json())