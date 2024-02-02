from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class TestLoginUi:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("http://demo.openemr.io/b/openemr/interface/login/login.php?site=default")
        yield
        self.driver.quit()

    def test_title(self):
        actual_title = self.driver.title
        assert_that("OpenEMR Login").__eq__(actual_title)

    def test_app_description(self):
        actual_desc = self.driver.find_element(By.XPATH, "//p[@class='text-center lead']").text
        assert_that(actual_desc).contains("Electronic Health Record")
