from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.__browser = driver

    def enter_username(self, username):
        self.__browser.find_element(By.ID, "authUser").send_keys(username)

    def enter_password(self, password):
        self.__browser.find_element(By.ID, "clearPass").send_keys(password)

    def click_login(self):
        self.__browser.find_element(By.ID, "login-button").click()

    def get_error_msg(self):
        error_msg = self.__browser.find_element(By.XPATH, "//*[contains(text(),'Invalid')]").text
        return error_msg

    def get_app_desc(self):
        return self.__browser.find_element(By.XPATH, "//p[@class='text-center lead']").text

    def get_username_placeholder(self):
        return self.__browser.find_element(By.ID, "authUser").get_attribute("placeholder")

    def get_password_placeholder(self):
        return self.__browser.find_element(By.ID, "clearPass").get_attribute("placeholder")

    @property
    def get_login_title(self):
        return self.__browser.title