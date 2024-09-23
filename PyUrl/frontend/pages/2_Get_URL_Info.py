import streamlit as st

from PyUrl.frontend.components import displays, forms, layout
from PyUrl.frontend.services import api_service

layout.add_custom_css()
layout.render_header()

st.title("Get URL Info")

code = forms.code_input_form()

if st.button("Get Info"):
    if code:
        result = api_service.get_url_info(code)
        displays.display_origin(result)
    else:
        st.error("Please enter a valid code.")

layout.render_footer()
