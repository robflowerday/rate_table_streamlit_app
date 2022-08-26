import streamlit as st


st.title("Rate table APR calculator")

st.file_uploader(
    label="Upload ods file here",
    type=['ods'],
)
