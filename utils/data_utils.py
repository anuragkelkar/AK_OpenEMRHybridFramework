import pandas
import pyarrow
import openpyxl
from utils import read_utils


class DataSource:
    """valid_testdata = [
        ("admin", "pass", "OpenEMR"),
        ("physician", "physician", "OpenEMR"),
        ("clinician", "clinician", "OpenEMR")
    ]
    invalid_testdata = [
        ("admin", "pass123", "Invalid username or password"),
        ("physician", "physician123", "Invalid username or password"),
        ("clinician123", "clinician", "Invalid username or password")
    ]"""
    valid_testdata = read_utils.get_excel_data_into_list("../test_data/login_testdata.xlsx", "valid_login")
    invalid_testdata = read_utils.get_excel_data_into_list("../test_data/login_testdata.xlsx", "invalid_login")
