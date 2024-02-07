from base.automation_wrapper import WebDriverWrapper
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_add_page import SearchAddPage
from utils.data_utils import DataSource
import pytest

class TestPatient(WebDriverWrapper):
    @pytest.mark.parametrize("username, password", DataSource.valid_login_data)
    def test_add_valid_patient(self,username,password):
        login = LoginPage(self.driver)
        main = MainPage(self.driver)
        search_page = SearchAddPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        main.click_on_patient_menu()
        main.click_on_new_search()
        search_page.enter_first_name("jack")
        search_page.enter_last_name("tod")
        search_page.enter_dob("13/1/2000")