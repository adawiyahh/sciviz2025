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
st.subheader("1. Academic Year Distribution")

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
The chart shows how Law students are distributed across different academic years. If there are more students in the first or second year, it may mean more new students have recently joined the program. Having fewer students in the final years could be because some have graduated or stopped studying. This helps the university see how many students continue each year and plan better for future intakes.
""")

# Best Aspects of the Program (Q7)
st.subheader("2. Best Aspects of the Law Program (Q7)")

best_aspects_counts = law_df['Q7. In your opinion,the best aspect of the program is'].value_counts()

# Create the chart
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=best_aspects_counts.index, y=best_aspects_counts.values, ax=ax)
ax.set_title('Most Common Best Aspects of the Law Program (Q7)')
ax.set_xlabel('Best Aspect')
ax.set_ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Display in Streamlit
st.pyplot(fig)

# Interpretation Section
st.markdown("### Interpretation")
st.write("""
The chart shows what Law students like most about their program. Common answers may include things like helpful lecturers, faculty, or resources. These responses highlight what students appreciate and what the program is doing well.
It also helps the university know which areas to maintain or improve to keep students satisfied.
""")

# Relationship Between Academic Year and Overall Satisfaction (Q5)
st.subheader("3. Relationship Between Academic Year and Overall Satisfaction (Q5)")

# Create the boxplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(
    data=law_df,
    x='Bachelor  Academic Year in EU',
    y='Q5 [To what extent your expectation was met?]',
    ax=ax
)
ax.set_title('Relationship Between Academic Year and Overall Satisfaction')
ax.set_xlabel('Academic Year')
ax.set_ylabel('Overall Satisfaction (Q5)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Display in Streamlit
st.pyplot(fig)

# Interpretation Section
st.markdown("### Interpretation")
st.write("""
The chart shows how Law students’ overall satisfaction changes by academic year. Most students, especially in the 1st, 2nd, and 4th years, rated their satisfaction quite high. However, 3rd-year students seem to have a wider range of satisfaction levels, with some giving lower ratings.This suggests that satisfaction may slightly drop in the middle years, possibly due to heavier workloads or more challenging courses.
""")

# Improvement in Education and University Image 
st.subheader("4. Improvement in Education and University Image")

# Calculate normalized percentages
education_improved_counts = law_df['Do you feel that the quality of education improved at EU over the last year?'].value_counts(normalize=True) * 100
image_improved_counts = law_df['Do you feel that the image of the University improved over the last year?'].value_counts(normalize=True) * 100

# Create side-by-side pie charts
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Pie chart 1: Education improved
axes[0].pie(
    education_improved_counts,
    labels=education_improved_counts.index,
    autopct='%1.1f%%',
    startangle=90
)
axes[0].set_title('Percentage of Law Students: Education Improved')
axes[0].axis('equal')

# Pie chart 2: University image improved
axes[1].pie(
    image_improved_counts,
    labels=image_improved_counts.index,
    autopct='%1.1f%%',
    startangle=90
)
axes[1].set_title('Percentage of Law Students: University Image Improved')
axes[1].axis('equal')

plt.tight_layout()

# Display in Streamlit
st.pyplot(fig)

# Interpretation Section
st.markdown("### Interpretation")
st.write("""
The charts show that most Law students believe both the quality of education and the university’s image have improved.
About 86.8% said the education improved, and nearly 89% agreed the university’s image got better.
Only a small number of students disagreed, meaning most students feel positive about the progress made. This suggests that recent efforts by the university are being noticed and appreciated by Law students.
""")

# Overall Satisfaction by Gender (Q5)
st.subheader("5. Overall Satisfaction by Gender (Q5)")

# Create the boxplot
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(
    data=law_df,
    x='Gender',
    y='Q5 [To what extent your expectation was met?]',
    ax=ax
)
ax.set_title('Overall Satisfaction by Gender in Law Faculty')
ax.set_xlabel('Gender')
ax.set_ylabel('Overall Satisfaction (Q5)')
plt.tight_layout()

# Display in Streamlit
st.pyplot(fig)

# Interpretation Section
st.markdown("### Interpretation")
st.write("""
The chart compares the overall satisfaction of male and female Law students. Both groups show generally high satisfaction, but male students seem to have slightly higher scores on average. There are a few male students who gave much lower ratings, shown as outliers. Overall, the results suggest that satisfaction levels are quite similar between genders, with only small differences.
""")
