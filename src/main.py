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

c1, c2 = st.columns((7,3))

with c2:
    st.markdown('### Donut chart')
    plost.donut_chart(
        data= state_data,
        theta= ['Active', 'Discharged', 'Deaths'],
        color=['#FFA500', '#FFD700', '#FF8C00'],
        legend='bottom', 
        use_container_width=True)

import matplotlib.pyplot as plt
 
# Setting labels for items in Chart
Employee = ['Roshni', 'Shyam', 'Priyanshi',
            'Harshit', 'Anmol']
 
# Setting size in Chart based on
# given values
Salary = [40000, 50000, 70000, 54000, 44000]
 
# colors
colors = ['#FF0000', '#0000FF', '#FFFF00',
          '#ADFF2F', '#FFA500']
# explosion
explode = (0.05, 0.05, 0.05, 0.05, 0.05)
 
# Pie Chart
plt.pie(Salary, colors=colors, labels=Employee,
        autopct='%1.1f%%', pctdistance=0.85,
        explode=explode)
 
# draw circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
 
# Adding Circle in Pie chart
fig.gca().add_artist(centre_circle)
 
# Adding Title of chart
plt.title('Employee Salary Details')
 
# Displaying Chart
plt.show()