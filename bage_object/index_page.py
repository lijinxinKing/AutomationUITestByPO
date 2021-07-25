from selenium.webdriver.common.by import By
from base.base_page import BasePage

class IndexPage(BasePage):
    BasePage.url = 'https://www.mi.com/?masid=2701.0074'
    input_el = (By.ID,'search')
    button = (By.XPATH,'//input[@class="search-btn iconfont"]')

    def search(self,txt):
        self.visit()
        self.input_(self.input_el,txt)
        self.click(self.button)
