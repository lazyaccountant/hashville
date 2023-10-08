import streamlit as st
from datetime import date, datetime
from sheets import ws, calc_bal

today = date.today()

def clear():
    st.session_state.date = today
    st.session_state.desc = ""
    st.session_state.amt = 0
    st.session_state.cat = "Select Category"
    st.session_state.notes = ""

st.title("Hashville🏠")

trans_date = st.date_input("Date", max_value=today, format="MM/DD/YYYY",key="date")
trans_date_str = datetime.strftime(trans_date, "%A, %B %d, %Y")

desc = st.text_input(label="Description", key="desc")

amt = st.number_input(label="Amount", key="amt")


categories = [
    "Infrastructure",
    "Preliminary Cost",
    "IT Digital/Physical Asset",
    "Inflow from Client",
    "Salary/Bonus",
    "Building Material",
    "Contractor Engagement",
    "Agency/Commission",
    "Demolition",
    "PR",
    "Survey",
    "Development Control",
    "Furniture/Asset",
    "Entertainment",
    "Printer & Stationery"
]
cat = st.selectbox(label="Category", options=["Select Category"]+categories, key="cat")

notes = st.text_area("Additional Notes", key="notes")

def save_trans():
    if desc == "":
        st.warning('Please enter description', icon="⚠️")
    elif amt == 0.00:
        st.warning('Please enter amount', icon="⚠️")
    elif cat == "Select Category":
        st.warning('Please enter category', icon="⚠️")
    else:
        if cat != "Inflow from Client":
            data = [trans_date_str, desc, amt, "", calc_bal(ws), cat, notes, "HASHVILLE"]
        else:
            data = [trans_date_str, desc, "", amt, calc_bal(ws), cat, notes, "HASHVILLE"]

        ws.append_row(data, value_input_option='USER_ENTERED')
        st.success('Transaction Saved!', icon="✅")
        clear()

save_button = st.button("Save", type="secondary", on_click=save_trans)

# host on streamlit