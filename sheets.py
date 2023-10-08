import gspread
from google.oauth2 import service_account
import streamlit as st

def load_ws():
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
    )

    gc = gspread.authorize(credentials)

    # Get the Google Sheet by URL.
    wb_url = st.secrets["public_gsheets_url"]
    wb = gc.open_by_url(wb_url)

    worksheet = wb.get_worksheet(0)

    return worksheet

def calc_bal(worksheet):
    # balance is on column 5, "E"
    values_list = worksheet.col_values(5)
    last_bal_row = len(values_list)
    new_bal = last_bal_row + 1
    bal_cell = f"=E{last_bal_row}+D{new_bal}-C{new_bal}"

    return bal_cell


ws = load_ws()