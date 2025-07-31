import streamlit as st

file_name = "generated_script.py"
file_content = 'print("This file was created in the app!")'

# Create a downloadable file
st.download_button(
    label="Download Python File",
    data=file_content,
    file_name=file_name,
    mime="text/x-python"
)
