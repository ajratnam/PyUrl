import streamlit as st

from PyUrl.frontend.components import layout

layout.add_custom_css()
layout.render_header()

st.title("Welcome to the URL Shortener App!")
st.markdown("""
### What is a URL Shortener?
A URL shortener is a tool that takes a long URL and converts it into a much shorter one.
This is especially useful when sharing links on social media, email, or text messages,
where character limits are important, or you just want to make the link more user-friendly.

### How Does it Work?
1. **Input a URL**: Provide a long URL that you want to shorten.
2. **Generate a Short URL**: The app will generate a unique, short code for the long URL.
3. **Retrieve Info**: You can look up the original URL using its short code anytime.
4. **Share the Short URL**: Use the shorter version in your messages or posts.

### Features
- **Shorten URLs**: Enter any URL, and this app will generate a shorter version.
- **Retrieve Original URLs**: Use a shortened code to get back to the original URL.
- **Built with FastAPI & Streamlit**: Leveraging modern web technologies for fast, reliable performance.

Use the sidebar to navigate to different features such as creating a short URL or getting info about a URL.
""")

st.info("🔍 Navigate through the features using the sidebar on the left.")

st.markdown("""
#### Why Use URL Shorteners?
- **Save Space**: Short URLs take up less space and are visually cleaner.
- **Track Clicks**: Many URL shorteners offer analytics to track how many people clicked the link.
- **Improve User Experience**: Short links are easier to read, understand, and share.

---

We hope this tool simplifies your experience with sharing long URLs!

""")

layout.render_footer()
