import pandas
import pyarrow
import openpyxl

import config
from utils import read_utils


class DataSource:
    valid_login_data = [
        ("admin", "pass")
    ]
    """
    invalid_testdata = [
        ("admin", "pass123", "Invalid username or password"),
        ("physician", "physician123", "Invalid username or password"),
        ("clinician123", "clinician", "Invalid username or password")
    ]"""
    valid_testdata = read_utils.get_excel_data_into_list(config.test_data_path+"/login_testdata.xlsx", "valid_login")
    invalid_testdata = read_utils.get_excel_data_into_list(config.test_data_path+"/login_testdata.xlsx", "invalid_login")
