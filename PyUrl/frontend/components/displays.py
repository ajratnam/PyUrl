import streamlit as st


def display_origin(result: dict) -> None:
    if "origin" in result:
        st.success(f"Original URL: {result['origin']}")
    else:
        st.error(result.get("detail", "An error occurred"))


def display_short(result: dict) -> None:
    if "url" in result:
        st.success(f"Shortened URL: {result['url']}")
    else:
        st.error(result.get("detail", "An error occurred"))
