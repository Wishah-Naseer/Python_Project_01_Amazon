import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


class GoogleSheet:
    def __init__(self, credentials_file, sheet_key):
        self.credentials_file = credentials_file
        self.sheet_key = sheet_key

        self.scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        self.sheet_object = self._get_sheet_object()

    def _get_sheet_object(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.credentials_file, self.scope
        )
        client = gspread.authorize(credentials)
        return client.open_by_key(self.sheet_key)

    def create_tabs(self, obj_link, tab_name):

        worsheet_list = obj_link.sheet_object.worksheets()
        tab_name_list = []
        for single_tab in worsheet_list:
            tab_name_list.append(single_tab.title)

        if tab_name in tab_name_list:
            print("already present")
            pass
        else:
            print("not present")
            worksheet = obj_link.sheet_object.add_worksheet(title=tab_name, rows="1000", cols="50")

    def read_data(self, obj_link, worksheet_name):
        previous_data = obj_link.sheet_object.worksheet(worksheet_name).get_all_values()
        if len(previous_data) == 0:
            print("Sheet is empty")
            pass
        else:
            #clear worksheet
            print("Sheet is not empty")
            obj_link.sheet_object.worksheet(worksheet_name).clear()
            print("Sheet cleared")

    def write_data(self,data,obj_link,tab_name,column,column_name):
        data = pd.DataFrame(data,columns=[column_name])
        set_with_dataframe(obj_link.sheet_object.worksheet(tab_name), dataframe=data, row=1, col=column)
