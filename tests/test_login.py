import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.automation_wrapper import WebDriverWrapper
from utils.data_utils import DataSource
from pages.login_page import LoginPage


# inherited class WebDriverWrapper class to reuse driver variable
class TestLoginFunction(WebDriverWrapper):

    @pytest.mark.parametrize("username, password, expected_title", DataSource.valid_testdata)
    def test_valid_login(self, username, password, expected_title):
        print("validation login")
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        assert_that(self.driver.title).matches(expected_title)

    @pytest.mark.parametrize("username, password, expected_title", DataSource.invalid_testdata)
    def test_invalid_login(self, username, password, expected_title):
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        error_msg = login.get_error_msg()
        assert_that(error_msg).is_equal_to(expected_title)

class TestLoginUi(WebDriverWrapper):
    def test_title(self):
        actual_title = self.driver.title
        assert_that("OpenEMR Login").matches(actual_title)

    def test_app_description(self):
        actual_desc = self.driver.find_element(By.XPATH, "//p[@class='text-center lead']").text
        assert_that(actual_desc).contains("Electronic Health Record")

    def test_placeholder(self):
        placeholder_value = self.driver.find_element(By.ID, "authUser").get_attribute("placeholder")
        assert_that(placeholder_value).__eq__("Username")
        placeholder_value2 = self.driver.find_element(By.ID, "clearPass").get_attribute("placeholder")
        assert_that(placeholder_value2).__eq__("Password")
        print(placeholder_value, placeholder_value2)
