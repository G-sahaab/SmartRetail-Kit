# dashboard_streamlit.py
# Streamlit App for Visualizing Retail Sales Dashboard

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Dashboard – SmartRetail-Kit")

# Load Excel
df = pd.read_excel("sales_dashboard.xlsx", sheet_name="Daily Sales")

# KPI Cards
total_sales = df["Revenue"].sum()
total_units = df["Quantity"].sum()
top_product = df.groupby("Product")["Revenue"].sum().idxmax()

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"₹{total_sales:,.0f}")
col2.metric("Units Sold", total_units)
col3.metric("Top Seller", top_product)

st.markdown("---")

# Revenue Over Time
line_chart = px.line(df, x="Date", y="Revenue", title="Daily Revenue Trend")
st.plotly_chart(line_chart, use_container_width=True)

# Revenue by Category
category_rev = df.groupby("Category")["Revenue"].sum().reset_index()
bar_chart = px.bar(category_rev, x="Category", y="Revenue", title="Revenue by Category", color="Category")
st.plotly_chart(bar_chart, use_container_width=True)

# Show Data Table
with st.expander("📄 View Raw Sales Data"):
    st.dataframe(df)
