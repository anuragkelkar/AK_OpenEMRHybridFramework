from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginUi:
    def test_title(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("http://demo.openemr.io/b/openemr/interface/login/login.php?site=default")
        actual_title = driver.title
        assert_that("OpenEMR Login").__eq__(actual_title)

    def test_app_description(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("http://demo.openemr.io/b/openemr/interface/login/login.php?site=default")
        actual_desc = driver.find_element(By.XPATH, "//p[@class='text-center lead']").text
        # assert actual_title.__eq__("OpenEMR Login")
        assert_that(actual_desc).contains("Electronic Health Record")
