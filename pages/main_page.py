from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.__browser = driver

    @property
    def get_main_title(self):
        return self.__browser.title

    def click_on_patient_menu(self):
        self.__browser.find_element(By.XPATH, "//div[text()=='Patient']").click()

    def click_on_new_search(self):
        self.__browser.find_element(By.XPATH, "//div[text()=='New/Search']").click()
