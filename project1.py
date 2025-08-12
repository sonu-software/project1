import streamlit as st
from playwright.sync_api import sync_playwright
import subprocess

def ensure_browsers_installed():
    try:
        subprocess.run(["playwright", "install", "chromium"], check=True)
    except Exception as e:
        st.error(f"Error installing browsers: {e}")

st.title("Headless Browser Screenshot")

ensure_browsers_installed()  # Install the browsers once

url = st.text_input("Enter URL", "https://example.com")

if st.button("Take Screenshot"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        screenshot = page.screenshot()
        browser.close()
    st.image(screenshot)
