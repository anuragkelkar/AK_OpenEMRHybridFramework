import pytest
from selenium import webdriver
import pandas
from utils import read_utils
import config

class WebDriverWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        #runs before each test method
        self.json_config = read_utils.get_json_data_into_dic(config.test_data_path+"\\config.json")
        browser = self.json_config.get("browser")
        if browser == "edge":
            self.driver=webdriver.Edge()
        elif browser == "ff":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get(self.json_config.get("url"))
        yield
        self.driver.quit()
