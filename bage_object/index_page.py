from selenium.webdriver.common.by import By
from base.base_page import BasePage

class IndexPage(BasePage):
    url = BasePage.url
    input_el = (By.NAME,'wd')
    button = (By.ID,'ai')

    def search(self,txt):
        self.visit()
        self.input_(self.input_el,txt)
        self.click(self.button)
