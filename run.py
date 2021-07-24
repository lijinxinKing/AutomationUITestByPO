# 生成测试报告 allure
# 1, 安装allure-pytets pip install allure-pytest
# 2, 下载一个commandline 包，放到Python 安装路径下
# 3, 配置 环境变量Path
# 4, 重启
import os

import pytest

if __name__ == '__main__':
    #数据目录，
    command_line = ["-s", "./test_case/test_case.py", "--alluredir=allure-result"]
    pytest.main(command_line)
    #生成测试报告 找到测试数据 生成测试报告 指定目录
    os.system('allure generate ./allure-result -o ./reports')
