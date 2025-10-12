import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Scientific Visualization")

st.header("Scientific Visualization", divider="gray")

# Upload dataset 
uploaded_file = st.file_uploader("Upload your Law Faculty dataset (CSV)", type="csv")

if uploaded_file is not None:
    # Read uploaded CSV into DataFrame
    law_df = pd.read_csv(uploaded_file)

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

else:
    st.warning("👆 Please upload a CSV file to visualize the data.")


