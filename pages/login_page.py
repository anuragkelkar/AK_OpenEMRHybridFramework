from selenium.webdriver.common.by import By
from base.webdriver_keywords import WebDriverKeywords


class LoginPage(WebDriverKeywords):
    def __init__(self, driver):
        super().__init__(driver)
        self.__browser = driver
        self.__username_locator = (By.ID, 'authUser')
        self.__password_locator =(By.ID, 'clearPass')
        self.__login_button_locator = (By.ID, 'login-button')
        self.__error_msg_locator = (By.XPATH, "//*[contains(text(),'Invalid')]")
        self.__app_desc_locator = (By.XPATH, "//p[@class='text-center lead']")

    def enter_username(self, username):
        # self.__browser.find_element(By.ID, "authUser").send_keys(username)
        super().type_on_element(self.__username_locator, username)

    def enter_password(self, password):
        # self.__browser.find_element(By.ID, "clearPass").send_keys(password)
        super().type_on_element(self.__password_locator, password)

    def click_login(self):
        # self.__browser.find_element(By.ID, "login-button").click()
        super().click_on_element(self.__login_button_locator)

    def get_error_msg(self):
        # error_msg = self.__browser.find_element(By.XPATH, "//*[contains(text(),'Invalid')]").text
        return super().get_text_from_element(self.__error_msg_locator)

    def get_app_desc(self):
        # return self.__browser.find_element(By.XPATH, "//p[@class='text-center lead']").text
        return super().get_text_from_element(self.__app_desc_locator)

    def get_username_placeholder(self):
        # return self.__browser.find_element(By.ID, "authUser").get_attribute("placeholder")
        return super().get_attribute_from_element(self.__username_locator, "placeholder")

    def get_password_placeholder(self):
        # return self.__browser.find_element(By.ID, "clearPass").get_attribute("placeholder")
        return super().get_attribute_from_element(self.__password_locator, "placeholder")

    @property
    def get_login_title(self):
        return self.__browser.title
