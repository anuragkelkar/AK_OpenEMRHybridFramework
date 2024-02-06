import pandas
import pyarrow
import openpyxl


# reusable methods for reading converting data from excel,json
def get_excel_data_into_list(
        excel_location, sheet_name):
    return pandas.read_excel(io=excel_location, sheet_name=sheet_name).values.tolist()
