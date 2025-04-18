import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Dashboard")

file_upload = st.file_uploader("Upload a File (CSV or XLSX)", type=["csv", "xlsx"])
if file_upload is not None:
    try:
        if file_upload.name.endswith(".csv"):
            df = pd.read_csv(file_upload)
        elif file_upload.name.endswith(".xlsx"):
            df = pd.read_excel(file_upload)
        st.write("✅ File Uploaded Successfully")

        if df.empty:
            st.warning("The uploaded file is empty.")
        else:
            # Display data preview and summary statistics
            st.subheader("Data Preview")
            st.dataframe(df)

            st.subheader("📊 Summary Statistics")
            st.write(df.describe())

            st.subheader("📊 Full Dataset Chart")
            numeric_cols = df.select_dtypes(include='number').columns.tolist()
            
            if numeric_cols:
                # Create a plot with matplotlib
                plt.figure(figsize=(10, 6))
                df[numeric_cols].plot(kind='line')  # Line plot for all numeric columns
                plt.title('Full Dataset Chart')
                plt.xlabel('Index')
                plt.ylabel('Values')
                plt.grid(True)
                
                # Display the plot
                st.pyplot(plt)
            else:
                st.warning("No numeric columns found for plotting.")

            st.subheader("⬇️ Download Data")
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='processed_data.csv',
                mime='text/csv',
            )     

    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    st.write("Waiting on File uploading")
