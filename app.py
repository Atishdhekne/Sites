import streamlit as st

# Read your HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Display in Streamlit
st.set_page_config(layout="wide")
st.components.v1.html(html_code, height=800, scrolling=True)
