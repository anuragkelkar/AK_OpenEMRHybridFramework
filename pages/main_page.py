from selenium.webdriver.common.by import By

from base.webdriver_keywords import WebDriverKeywords


class MainPage(WebDriverKeywords):
    def __init__(self, driver):
        super().__init__(driver)
        self.__browser = driver
        self.__patient_menu_locator=(By.XPATH, "//div[text()=='Patient']")
        self.__new_search_menu_locator =(By.XPATH, "//div[text()=='New/Search']")

    def get_main_title(self):
        return self.__browser.title

    def click_on_patient_menu(self):
        super().click_on_element(self.__patient_menu_locator)

    def click_on_new_search(self):
        super().click_on_element(self.__new_search_menu_locator)
