import streamlit as st
from playwright.sync_api import sync_playwright
import base64

st.title("Headless Browser Screenshot with Playwright")

url = st.text_input("Enter URL to screenshot")

if st.button("Take Screenshot"):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        screenshot_bytes = page.screenshot()
        browser.close()
    
    st.image(screenshot_bytes)
    b64 = base64.b64encode(screenshot_bytes).decode()
    href = f'<a href="data:file/png;base64,{b64}" download="screenshot.png">Download screenshot</a>'
    st.markdown(href, unsafe_allow_html=True)


