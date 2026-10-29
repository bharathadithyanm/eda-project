import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Page configuration
st.set_page_config(page_title="EDA Project", layout="wide")

# Title
st.title("📊 Exploratory Data Analysis (EDA) Project")

st.write("Analyze datasets to uncover patterns and trends.")

# File uploader
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:

    # Load dataset
    df = pd.read_csv(uploaded_file)

    # Show dataset
    st.subheader("📌 Dataset Preview")
    st.dataframe(df.head())

    # Dataset information
    st.subheader("📌 Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

    with col2:
        st.write("Missing Values:")
        st.write(df.isnull().sum())

    # Statistical summary
    st.subheader("📌 Statistical Summary")
    st.dataframe(df.describe())

    # Data Cleaning
    st.subheader("📌 Data Cleaning")

    missing_values = df.isnull().sum().sum()

    if missing_values > 0:
        df = df.dropna()
        st.success(f"Removed {missing_values} missing values.")
    else:
        st.success("No missing values found.")

    # Correlation Heatmap
    st.subheader("📌 Correlation Heatmap")

    numeric_df = df.select_dtypes(include=['number'])

    if not numeric_df.empty:

        corr = numeric_df.corr()

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

        st.pyplot(fig)

    else:
        st.warning("No numeric columns found for correlation.")

    # Histogram
    st.subheader("📌 Distribution Plot")

    numeric_columns = numeric_df.columns.tolist()

    if numeric_columns:

        selected_column = st.selectbox(
            "Select Column",
            numeric_columns
        )

        fig2 = px.histogram(
            df,
            x=selected_column,
            title=f"Distribution of {selected_column}",
            nbins=20
        )

        st.plotly_chart(fig2, use_container_width=True)

    # Scatter Plot
    st.subheader("📌 Scatter Plot")

    if len(numeric_columns) >= 2:

        x_axis = st.selectbox("Select X-axis", numeric_columns)
        y_axis = st.selectbox("Select Y-axis", numeric_columns, index=1)

        fig3 = px.scatter(
            df,
            x=x_axis,
            y=y_axis,
            title=f"{x_axis} vs {y_axis}",
            color=y_axis
        )

        st.plotly_chart(fig3, use_container_width=True)

    # Insights
    st.subheader("📌 Key Insights")

    st.write("""
    ✅ Dataset cleaned successfully  
    ✅ Statistical summary generated  
    ✅ Correlation between variables identified  
    ✅ Distribution and trends visualized  
    ✅ Patterns analyzed using charts and graphs
    """)

else:
    st.info("Please upload a CSV file to begin analysis.")