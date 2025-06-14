# 需求：登录成功

# 导包
import requests

# 发送请求
base_url = "http://localhost:8080/oauth/token"
header_data = {
    "Content-Type": "application/json"
}

login_data = {
    "username": "xiongshibao2",
    "password": "xiongshibao2",  # 使用明文密码
    "grant_type":"password",
    "client_id":"bookstore_frontend",
    "client_secret":"bookstore_secret"
}

# 构建完整的URL（将参数拼接在URL后面）
params = []
for key, value in login_data.items():
    params.append(f"{key}={value}")
url = f"{base_url}?{'&'.join(params)}"

# 打印完整的请求URL和参数
print("完整的请求URL和参数：")
print(f"URL: {url}")
print("参数:")
for key, value in login_data.items():
    print(f"{key}: {value}")

response = requests.get(url=url, headers=header_data)

# 查看响应
print("\n响应状态码：")
print(response.status_code)
print("\n响应内容：")
print(response.json())

