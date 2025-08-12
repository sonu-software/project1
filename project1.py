import streamlit as st
from playwright.sync_api import sync_playwright

st.title("Open a Link using Playwright in Streamlit")

url = st.text_input("Enter URL to open", "https://example.com")

if st.button("Open Link"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        title = page.title()
        st.write(f"Page title: {title}")
        browser.close()
