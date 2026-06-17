import streamlit as st
import pandas as pd

# Set up the webpage
st.set_page_config(
    page_title="My CSV Dashboard",
    page_icon="📊",
    layout="wide"
)

# Dashboard title
st.title("📊 My CSV Dashboard")

st.write("This dashboard displays information from my CSV file.")

# Read the CSV file
df = pd.read_csv("plants.csv")

# Show three summary numbers
column1, column2, column3 = st.columns(3)

column1.metric("Rows", len(df))
column2.metric("Columns", len(df.columns))
column3.metric("Missing values", int(df.isna().sum().sum()))

# Show the CSV as a table
st.subheader("Dataset")

st.dataframe(
    df,
    use_container_width=True
)

# Let the viewer choose a column
st.subheader("Explore the data")

selected_column = st.selectbox(
    "Choose a column:",
    df.columns
)

# Count the values in the selected column
chart_data = (
    df[selected_column]
    .dropna()
    .value_counts()
    .head(20)
)

# Show the results as a bar chart
st.bar_chart(chart_data)
