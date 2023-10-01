import streamlit as st
import pandas as pd
import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('../visualytics/src/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard `version 0`')

st.sidebar.subheader('Covid-19 parameters')

#Load data
state_wise = pd.read_csv('../visualytics/datasets/2/state_wise.csv')

# Get selected state
selected_state = st.sidebar.selectbox('Select `state/UTs`', state_wise['State/UTs'].unique())

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

st.sidebar.markdown('''
---
Created with ❤️ by Ayush Kumar
''')


# Row A
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


# Filter data for selected state
state_data = state_wise[state_wise['State/UTs'] == selected_state]
