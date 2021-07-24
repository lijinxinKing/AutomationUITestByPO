from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    # 页面的URL
    url = BasePage.url + ''
    # 页面中关联的元素对象
    user = (By.XPATH, '//*[@name="account"]')
    pwd = (By.XPATH, '//*[@name="password"]')
    button = (By.XPATH, '//*[@type="submit"]')

    def login(self, account, password):
        self.visit()
        sleep(10)
        self.input_(self.user, account)
        self.input_(self.pwd, password)
        self.click(self.button)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    account = ''
    password = ''
    lp = LoginPage(driver)
    lp.login(account,password)
