import streamlit as st
import pandas as pd

def load_data():
    df = pd.read_csv('/home/zerocool/git/visualytics/datasets/2/Latest Covid-19 India Status.csv')
    return df

df = load_data()

st.write("Displaying the CSV file:")
st.write(df)