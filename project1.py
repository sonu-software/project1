import streamlit as st
import streamlit.components.v1 as components


st.markdown("""
<h1 style='color:blue'>Welcome to CyberSRC Labs</h1>
<p>This is a sample paragraph.</p>
""", unsafe_allow_html=True)






html_code = open("facebook.html", "r", encoding="utf-8").read()
components.html(html_code, height=1000, scrolling=True)

