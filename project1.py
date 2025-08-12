import streamlit as st
from playwright.sync_api import sync_playwright
import subprocess

# Run this once to install browser binaries in the current environment
def install_browsers():
    try:
        result = subprocess.run(["playwright", "install", "chromium"], capture_output=True, text=True, check=True)
        st.write(result.stdout)
    except subprocess.CalledProcessError as e:
        st.error(f"Browser install failed:\n{e.stderr}")

st.title("Playwright Screenshot App")

# Run browser install once at app start
install_browsers()

url = st.text_input("Enter URL", "https://example.com")

if st.button("Take Screenshot"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        screenshot = page.screenshot()
        browser.close()
    st.image(screenshot)
