import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Set page config
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

st.sidebar.header('Covid-19 Dashboard')
st.sidebar.markdown('''
---
Created with ❤️ by Ayush Kumar & Kekma
''')

# Directory containing CSV files
data_dir = "/home/zerocool/git/visualytics/datasets/"

# Get list of CSV files
csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]

# Get selected file from dropdown
selected_file = st.sidebar.selectbox('Select CSV file', csv_files)

# Load data
data_url = os.path.join(data_dir, selected_file)
df = pd.read_csv(data_url)

# Visualizations for first CSV file
if selected_file == '1.csv':
    # Reshape data for line chart
    df_melt = df.melt(id_vars='Date', value_vars=['Confirmed'], var_name='case', value_name='count')

    # Display line chart
    st.markdown('### Trend of Confirmed Cases over Time')
    fig = px.line(df_melt, x='Date', y='count', color='case',
                  title='Trend of Confirmed Cases over Time')
    st.plotly_chart(fig, use_container_width=True)

    # Reshape data for bar chart
    df_bar = df.groupby('State/UnionTerritory')['Confirmed'].max().reset_index()

    # Display bar chart
    st.markdown('### Number of Confirmed Cases by State/UTs')
    fig = px.bar(df_bar, x='State/UnionTerritory', y='Confirmed',
                 title='Number of Confirmed Cases by State/UTs')
    st.plotly_chart(fig, use_container_width=True)

# Visualizations for second CSV file
elif selected_file == '2.csv':
    # Reshape data for bar chart
    df_bar = df[['State/UTs', 'Total Cases']].sort_values('Total Cases', ascending=False)

    # Display bar chart
    st.markdown('### Number of Total Cases by State/UTs')
    fig = px.bar(df_bar, x='State/UTs', y='Total Cases',
                 title='Number of Total Cases by State/UTs')
    st.plotly_chart(fig, use_container_width=True)

    # Reshape data for scatter plot
    df_scatter = df[['State/UTs', 'Total Cases', 'Population']]
    df_scatter['Cases per Million'] = df_scatter['Total Cases'] / (df_scatter['Population'] / 1000000)

    # Display scatter plot
    st.markdown('### Relationship between Population and Total Cases')
    fig = px.scatter(df_scatter, x='Population', y='Total Cases', size='Cases per Million',
                     title='Relationship between Population and Total Cases')
    st.plotly_chart(fig, use_container_width=True)

    # Reshape data for pie chart
    df_pie = df[['State/UTs', 'Total Cases']].sort_values('Total Cases', ascending=False).head(10)

    # Display pie chart
    st.markdown('### Top 10 States with Highest Total Cases')
    fig = px.pie(df_pie, values='Total Cases', names='State/UTs',
                 title='Top 10 States with Highest Total Cases')
    st.plotly_chart(fig, use_container_width=True)