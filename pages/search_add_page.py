from selenium.webdriver.common.by import By
from base.webdriver_keywords import WebDriverKeywords


class SearchAddPage(WebDriverKeywords):
    def __init__(self, driver):
        super().__init__(driver)
        self.__browser = driver
        self.__firstname_locator = (By.ID, 'form_fname')
        self.__lastname_locator =(By.ID, 'form_lname')
        self.DOB_locator = (By.NAME, 'form_DOB')

    def enter_first_name(self,first_name):
        self.__browser.switch_to.frame(self.__browser.find_element(By.NAME,"pat"))
        super().type_on_element(self.__firstname_locator,first_name)

    def enter_last_name(self,last_name):
        self.__browser.switch_to.frame(self.__browser.find_element(By.NAME,"pat"))
        super().type_on_element(self.__firstname_locator,last_name)

    def enter_dob(self,last_DOB):
        self.__browser.switch_to.frame(self.__browser.find_element(By.NAME,"pat"))
        super().type_on_element(self.DOB_locator,last_DOB)