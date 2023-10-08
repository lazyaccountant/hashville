import streamlit as st
from datetime import date

today = date.today()


def clear():
    st.session_state.date = today
    st.session_state.desc = ""
    st.session_state.amt = 0
    st.session_state.cat = "Select Category"
    st.session_state.notes = ""

st.title("Hashville🏠")

trans_date = st.date_input("Date", max_value=today, format="MM/DD/YYYY",key="date")

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
        st.success('Transaction Saved!', icon="✅")
        data = [trans_date, desc, amt, cat, notes]
        print(data)
        clear()

save_button = st.button("Save", type="secondary", on_click=save_trans)

# create private git repo
# input google sheet credentials in secrets.toml
# add append function
# host on streamlit