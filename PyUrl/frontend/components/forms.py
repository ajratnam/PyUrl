import streamlit as st


def url_input_form() -> tuple[str, str]:
    url = st.text_input("Enter the original URL")
    custom_code = st.text_input("Custom short code (optional)")
    return url, custom_code


def code_input_form() -> str:
    code = st.text_input("Enter the short code")
    return code
