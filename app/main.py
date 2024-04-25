import datetime
import re
import matplotlib.pyplot as plt
import utils
import streamlit as st
import pandas as pd


st.title("Data Insights Dashboard")

selected_option = st.selectbox(label="Choose data:", options=utils.get_list_of_csvs())

df = utils.fetch_data(f"./data/{selected_option}")

st.title("Data Visualization Dashboard")
st.markdown(
    "This dashboard allows you to visualize data with various interactive features."
)

data = utils.clean_data(df)

st.sidebar.header("Customize the Dashboard")
plot_type = st.sidebar.selectbox(
    "Select Plot Type", ["Line Plot", "Scatter Plot", "Box Plot", "Histogram"]
)

x_column = st.sidebar.selectbox("X-Axis", data.columns)
y_column = st.sidebar.selectbox("Y-Axis", data.columns)

if plot_type == "Line Plot":
    utils.generate_line_plot(data, x_column, y_column, "Line Plot")

elif plot_type == "Scatter Plot":
    hue_column = st.sidebar.selectbox("Hue", ["None"] + list(data.columns))
    hue = None if hue_column == "None" else hue_column
    utils.generate_scatter_plot(data, x_column, y_column, "Scatter Plot", hue=hue)

elif plot_type == "Box Plot":
    utils.generate_box_plot(data, x_column, "Box Plot")

elif plot_type == "Histogram":
    utils.generate_histogram(data, x_column, "Histogram")

st.header("Summary Statistics")
st.write(utils.get_summary_stats(data))

st.subheader("Time Series Analysis")
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df.set_index("Timestamp", inplace=True)
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(df["GHI"], color="blue")
plt.title("Global Horizontal Irradiance (GHI)")
plt.xlabel("Timestamp")
plt.ylabel("GHI")

st.pyplot(plt)

st.subheader("Data Quality Check")
category = st.selectbox("Select Category", ["Missing values", "Negative values"])
filtered_data = None
if category == "Missing values":
    filtered_data = df.isnull().sum()
if category == "Negative values":
    filtered_data = df[(df["GHI"] < 0) | (df["DNI"] < 0) | (df["DHI"] < 0)]

st.write(filtered_data)
