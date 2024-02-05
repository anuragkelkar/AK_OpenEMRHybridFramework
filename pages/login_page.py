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
