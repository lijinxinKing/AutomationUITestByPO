from time import sleep
import pytest
from selenium import webdriver

from bage_object.index_page import IndexPage
from bage_object.login_page import LoginPage
from config.yamlload import loadyaml

class TestDemo:
    def setup_class(cls) -> None:
        cls.driver = webdriver.Chrome('./tool/chromedriver.exe')
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPage(cls.driver)

    def teardown_class(cls) -> None:
        sleep(3)
        cls.driver.quit()

    @pytest.mark.parametrize('udata',loadyaml('./data/login.yaml'))
    def test_login(self,udata):
        self.lp.login(udata['account'],udata['password'])

    def test_login1(self):
        assert 1 == 1

    @pytest.mark.parametrize('udata', loadyaml('./data/search.yaml'))
    def test_login2(self,udata):
        self.ip.search(udata['txt'])

if __name__ == '__main__':
    pytest.main()