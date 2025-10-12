import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")


# Assuming 'law_df' is already defined
gender_counts = law_df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

# Create pie chart using Plotly
fig = px.pie(
    gender_counts,
    names='Gender',
    values='Count',
    title='Gender Distribution in Law Faculty',
    hole=0,  # 0 means full pie (1 means donut)
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)






# Assuming 'law_df' is already defined
gender_counts = law_df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

# Create bar chart using Plotly
fig = px.bar(
    gender_counts,
    x='Gender',
    y='Count',
    title='Gender Distribution in Law Faculty',
    text='Count',
    color='Gender'
)

# Customize layout
fig.update_layout(
    xaxis_title='Gender',
    yaxis_title='Count',
    xaxis_tickangle=0
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)


