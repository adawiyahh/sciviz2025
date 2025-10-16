import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Scientific Visualization")

st.header("Scientific Visualization", divider="gray")

# Load dataset from GitHub 
# Replace this URL with your actual raw CSV file link
csv_url = "https://raw.githubusercontent.com/adawiyahh/sciviz2025/refs/heads/main/law_faculty_survey.csv"

# Read dataset directly from GitHub
law_df = pd.read_csv(csv_url)
st.dataframe(law_df)

# Gender Distribution Pie Chart 
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

# Gender Distribution Bar Chart 
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

# Visualization Section
st.markdown("## Visualization")

# Academic Year Distribution (Matplotlib + Seaborn)
st.subheader("Academic Year Distribution")

academic_year_counts = law_df['Bachelor  Academic Year in EU'].value_counts()

# Create the chart
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=academic_year_counts.index, y=academic_year_counts.values, ax=ax)
ax.set_title('Academic Year Distribution in Law Faculty')
ax.set_xlabel('Academic Year')
ax.set_ylabel('Count')
plt.xticks(rotation=45, ha='right')

# Display the chart in Streamlit
st.pyplot(fig)

# Interpretation Section
st.markdown("### Interpretation")
st.write("""
The chart shows how Law students are distributed across different academic years.  
If there are more students in the first or second year, it may mean more new students have recently joined the program.  
Having fewer students in the final years could be because some have graduated or stopped studying.  
This helps the university understand student retention and plan for future intakes.
""")


