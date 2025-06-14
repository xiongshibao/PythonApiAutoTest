# 需求：登录成功

# 导包
import requests

# 发送请求
base_url = "http://localhost:8080/restful/accounts/"
header_data = {
    "Content-Type": "application/json"
}

register_data = {
    "username": "xiongshibao",
    "password": "xiongshibao",
    "name": "xiongshibao",
    "telephone": "18990000333",
    "email": "xiongshibao2222@163.com"
}

response = requests.post(url=base_url, headers=header_data, json=register_data)

# 查看响应
print("\n响应状态码：")
print(response.status_code)
print("\n响应内容：")
print(response.json())
