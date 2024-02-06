import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.automation_wrapper import WebDriverWrapper
from utils.data_utils import DataSource
from pages.login_page import LoginPage
from pages.main_page import MainPage


# inherited class WebDriverWrapper class to reuse driver variable
class TestLoginFunction(WebDriverWrapper):

    @pytest.mark.parametrize("username, password, expected_title", DataSource.valid_testdata)
    def test_valid_login(self, username, password, expected_title):
        print("validation login")
        login = LoginPage(self.driver)
        main = MainPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        assert_that(main.get_main_title()).matches(expected_title)

    @pytest.mark.parametrize("username, password, expected_error", DataSource.invalid_testdata)
    def test_invalid_login(self, username, password, expected_error):
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        error_msg = login.get_error_msg()
        assert_that(error_msg).is_equal_to(expected_error)


class TestLoginUi(WebDriverWrapper):
    def test_title(self):
        login = LoginPage(self.driver)
        assert_that("OpenEMR Login").matches(login.get_login_title)

    def test_app_description(self):
        login = LoginPage(self.driver)
        actual_desc = login.get_app_desc()
        assert_that(actual_desc).contains("Electronic Health Record")

    def test_placeholder(self):
        login = LoginPage(self.driver)
        username_placeholder = login.get_username_placeholder()
        password_placeholder = login.get_password_placeholder()
        assert_that(username_placeholder).is_equal_to("Username")
        assert_that(password_placeholder).is_equal_to("Password")
