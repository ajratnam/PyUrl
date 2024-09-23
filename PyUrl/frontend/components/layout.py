import streamlit as st


def add_custom_css() -> None:
    st.markdown(
        """
    <style>
    .header {
        background: linear-gradient(135deg, #6db3f2 0%, #1e69de 100%);
        padding: 20px;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 25px;
    }
    .header h2 {
        color: white;
        font-family: 'Arial', sans-serif;
        font-size: 32px;
    }

    .footer {
        text-align: center;
        padding: 10px 0;
        margin-top: 25px;
        color: #a0a0a0;
        font-size: 14px;
        border-top: 1px solid #393939;
    }

    .stTextInput > div > input {
        background-color: #333;
        color: white;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


def render_header() -> None:
    st.markdown(
        """
    <div class="header">
        <h2>🚀 URL Shortener App</h2>
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_footer() -> None:
    st.markdown(
        """
    <div class="footer">
        © 2024 URL Shortener App. Built with ❤️ using FastAPI & Streamlit.
    </div>
    """,
        unsafe_allow_html=True,
    )
