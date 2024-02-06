from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WebDriverKeywords:
    def __init__(self, driver):
        self.__browser = driver
        self.wait = WebDriverWait(self.__browser, 30)

    def type_on_element(self, locator, value):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).send_keys(value)

    def click_on_element(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).click()

    def get_text_from_element(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).text

    def get_attribute_from_element(self,locator,key):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).get_attribute(key)

