'''
封装浏览器基本操作
公共方法：等待时间，截图，点击，日志，浏览器所有操作
需求：任何点击，自动去加等待时间
关键字驱动：
    公共方法关键字：
    业务关键字：操作经常绑定在一起的，封装成关键字
'''
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
import os
import allure

class BasePage:
    # driver = webdriver.Chrome()
    url = ''
    def __init__(self, driver):
        filePath = './tools/chromedriver.exe'
        self.driver = driver  # webdriver.Chrome(filePath)

    # 访问URL
    def visit(self):
        self.driver.get(self.url)

    # 元素的定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 元素的输入行为
    def input_(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 元素的点击行为
    def click(self, loc):
        self.locator(loc).click()

    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self,item, call):
        '''
        获取每个用例状态的钩子函数
        :param item:
        :param call:
        :return:
        '''
        # 获取钩子方法的调用结果
        outcome = yield
        rep = outcome.get_result()
        # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
        if rep.when == "call" and rep.failed:
            mode = "a" if os.path.exists("failures") else "w"
            with open("failures", mode) as f:
                # let's also access a fixture for the fun of it
                if "tmpdir" in item.fixturenames:
                    extra = " (%s)" % item.funcargs["tmpdir"]
                else:
                    extra = ""
                f.write(rep.nodeid + extra + "\n")
            # 添加allure报告截图
            if hasattr(self.driver, "get_screenshot_as_png"):
                with allure.step('添加失败截图...'):
                    allure.attach(self.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)