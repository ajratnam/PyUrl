import streamlit as st

from PyUrl.frontend.components import displays, forms, layout
from PyUrl.frontend.services import api_service

layout.add_custom_css()
layout.render_header()

st.title("Shorten URL")

url, custom_code = forms.url_input_form()

if st.button("Shorten URL"):
    if url:
        result = api_service.shorten_url(url, custom_code)
        displays.display_short(result)
    else:
        st.error("Please enter a valid URL.")

layout.render_footer()
