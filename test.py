import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Scientific Visualization")

st.header("Scientific Visualization", divider="gray")

# ---- Load dataset from GitHub ----
# 🔹 Replace this URL with your actual raw CSV file link
csv_url = "https://raw.githubusercontent.com/adawiyahh/sciviz2025/refs/heads/main/law_faculty_survey.csv"

# Read dataset directly from GitHub
law_df = pd.read_csv(csv_url)

# ---- Gender Distribution Pie Chart ----
gender_counts = law_df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

fig_pie = px.pie(
    gender_counts,
    names='Gender',
    values='Count',
    title='Gender Distribution in Law Faculty',
    hole=0  # 0 = full pie, 1 = donut
)
st.plotly_chart(fig_pie, use_container_width=True)

# ---- Gender Distribution Bar Chart ----
fig_bar = px.bar(
    gender_counts,
    x='Gender',
    y='Count',
    title='Gender Distribution in Law Faculty',
    text='Count',
    color='Gender'
)
fig_bar.update_layout(
    xaxis_title='Gender',
    yaxis_title='Count',
    xaxis_tickangle=0
)
st.plotly_chart(fig_bar, use_container_width=True)


