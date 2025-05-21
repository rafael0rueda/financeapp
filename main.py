import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

st.set_page_config(page_title="Finance Dashboard", page_icon="💰", layout="wide")

def load_transactions(file):
    try:
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns]
        #df["Amount"] = df["Amount"].str.replace(",","").astype(float)
        df["Amount"] = df["Amount"].astype(float)
        df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
        #st.write(df)
        return df
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None

def main():
    st.title("Finance Dashboard")

    uploaded_file = st.file_uploader("Upload your transaction CSV file", type=["csv"])

    if uploaded_file is not None:
        df = load_transactions(uploaded_file)

        if df is not None:
            debits_df = df[df["Debit/Credit"] == "Debit"].copy()
            credit_df = df[df["Debit/Credit"] == "Credit"].copy()

            tab1, tab2 = st.tabs(["Expenses (Debits)", "Credits"])
            with tab1:
                st.write(debits_df)
            with tab2:
                st.write(credit_df)

main()
