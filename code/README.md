allure配置

要使用这些配置，请按照以下步骤操作：

1. 首先确保您的测试文件中的中文注释和描述使用 UTF-8 编码保存。

2. 运行测试时使用以下命令：
```bash
pytest --alluredir=report --clean-alluredir
```

3. 生成报告时使用：
```bash
allure generate report -o report/html --clean
```

4. 查看报告：
```bash
allure serve report
```

如果仍然遇到中文显示问题，您可以尝试以下解决方案：

1. 在测试文件中添加编码声明：
```python
# -*- coding: utf-8 -*-
```

2. 确保您的测试用例描述使用 `@allure.description` 装饰器：
```python
import allure

@allure.feature("登录功能")
@allure.story("用户登录")
@allure.description("测试用户登录功能")
def test_login():
    pass
```

3. 如果使用 Windows 系统，可以在运行 Allure 命令前设置环境变量：
```bash
set PYTHONIOENCODING=utf-8
```

4. 如果使用的是 Allure 命令行工具，可以尝试使用最新版本：
```bash
pip install --upgrade allure-pytest
```

