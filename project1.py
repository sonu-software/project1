import streamlit as st
import streamlit.components.v1 as components


html_code = open("facebook.html", "r", encoding="utf-8").read()
components.html(html_code, height=3000,width=1000)






