from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from base.automation_wrapper import WebDriverWrapper


# inherited class WebDriverWrapper class to reuse driver variable
class TestLoginFunction(WebDriverWrapper):
    def test_valid_login(self):
        print("validation login")
        self.driver.find_element(By.ID, "authUser").send_keys("admin")
        self.driver.find_element(By.ID, "clearPass").send_keys("pass")
        self.driver.find_element(By.ID,"login-button").click()
        actual_title = self.driver.title
        print(actual_title)
        assert_that(actual_title).matches("OpenEMR")


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
