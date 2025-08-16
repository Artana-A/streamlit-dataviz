<<<<<<< HEAD
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from io import BytesIO

st.title("📊 Data Visualization Dashboard")

# File upload
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Read file
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    # Show preview
    st.write("### Data Preview", df.head())

    # Chart options in sidebar
    st.sidebar.title("Chart Settings")
    chart_type = st.sidebar.selectbox(
        "Select chart type",
        ["Line", "Bar", "Scatter", "Seaborn Heatmap", "Plotly Interactive"]
    )
    x_axis = st.sidebar.selectbox("Select X-axis", df.columns)
    y_axis = st.sidebar.selectbox("Select Y-axis", df.columns)

    # Handle NaNs
    filtered_df = df.dropna(subset=[x_axis, y_axis])

    # Draw charts
    if chart_type == "Line":
        fig, ax = plt.subplots()
        ax.plot(filtered_df[x_axis], filtered_df[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        st.pyplot(fig)

    elif chart_type == "Bar":
        fig, ax = plt.subplots()
        ax.bar(filtered_df[x_axis], filtered_df[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        st.pyplot(fig)

    elif chart_type == "Scatter":
        fig, ax = plt.subplots()
        ax.scatter(filtered_df[x_axis], filtered_df[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        st.pyplot(fig)

    elif chart_type == "Seaborn Heatmap":
        numeric_df = df.select_dtypes(include=['number'])
        if numeric_df.shape[1] < 2:
            st.warning("Heatmap requires at least 2 numeric columns.")
        else:
            fig, ax = plt.subplots()
            sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

    elif chart_type == "Plotly Interactive":
        color_col = st.sidebar.selectbox("Color by (optional)", [None] + list(df.columns))
        fig = px.scatter(filtered_df, x=x_axis, y=y_axis, color=color_col if color_col else None)
        st.plotly_chart(fig)

    # Download filtered data
    st.subheader("📥 Download Filtered Data")
    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download as CSV",
        data=csv_data,
        file_name="filtered_data.csv",
        mime="text/csv"
    )

else:
    st.info("📥 Please upload a CSV or Excel file to get started.")
=======
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("📊 Data Visualization Dashboard")

# File upload
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Read file
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    # Show preview
    st.write("### Data Preview", df.head())

    # ------------------------------
    # 🔹 WIDGETS SECTION
    # ------------------------------

    # Checkbox to show full dataset
    if st.checkbox("Show full dataset"):
        st.write(df)

    # Multiselect filter for categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    if categorical_cols:
        filter_col = st.selectbox("Select column to filter", categorical_cols)
        unique_vals = df[filter_col].unique()
        selected_vals = st.multiselect(f"Filter {filter_col}", unique_vals, default=unique_vals)
        df = df[df[filter_col].isin(selected_vals)]

    # Slider filter for numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    if numeric_cols:
        num_col = st.selectbox("Select numeric column to filter", numeric_cols)
        min_val, max_val = float(df[num_col].min()), float(df[num_col].max())
        selected_range = st.slider(f"Filter {num_col}", min_val, max_val, (min_val, max_val))
        df = df[(df[num_col] >= selected_range[0]) & (df[num_col] <= selected_range[1])]

    # Sorting
    sort_col = st.selectbox("Sort by column", df.columns)
    sort_order = st.radio("Sort order", ["Ascending", "Descending"])
    df = df.sort_values(by=sort_col, ascending=(sort_order == "Ascending"))

    # ------------------------------
    # 🔹 CHART SETTINGS & PLOTTING
    # ------------------------------
    st.sidebar.title("Chart Settings")
    chart_type = st.sidebar.selectbox(
        "Select chart type",
        ["Line", "Bar", "Scatter", "Seaborn Heatmap", "Plotly Interactive"]
    )
    x_axis = st.sidebar.selectbox("Select X-axis", df.columns)
    y_axis = st.sidebar.selectbox("Select Y-axis", df.columns)

    # Handle NaNs
    filtered_df = df.dropna(subset=[x_axis, y_axis])

    # Draw charts
    if chart_type == "Line":
        fig, ax = plt.subplots()
        ax.plot(filtered_df[x_axis], filtered_df[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        st.pyplot(fig)

    elif chart_type == "Bar":
        fig, ax = plt.subplots()
        ax.bar(filtered_df[x_axis], filtered_df[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        st.pyplot(fig)

    elif chart_type == "Scatter":
        fig, ax = plt.subplots()
        ax.scatter(filtered_df[x_axis], filtered_df[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        st.pyplot(fig)

    elif chart_type == "Seaborn Heatmap":
        numeric_df = df.select_dtypes(include=['number'])
        if numeric_df.shape[1] < 2:
            st.warning("Heatmap requires at least 2 numeric columns.")
        else:
            fig, ax = plt.subplots()
            sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

    elif chart_type == "Plotly Interactive":
        color_col = st.sidebar.selectbox("Color by (optional)", [None] + list(df.columns))
        fig = px.scatter(filtered_df, x=x_axis, y=y_axis, color=color_col if color_col else None)
        st.plotly_chart(fig)

    # ------------------------------
    # 🔹 DOWNLOAD FILTERED DATA
    # ------------------------------
    st.subheader("📥 Download Filtered Data")
    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download as CSV",
        data=csv_data,
        file_name="filtered_data.csv",
        mime="text/csv"
    )

else:
    st.info("📥 Please upload a CSV or Excel file to get started.")
>>>>>>> da05f44 (Update with new widgets)
