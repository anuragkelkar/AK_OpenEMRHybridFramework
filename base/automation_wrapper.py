import pytest
from selenium import webdriver
class WebDriverWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("http://demo.openemr.io/b/openemr/interface/login/login.php?site=default")
        yield
        self.driver.quit()
