import streamlit as st
from playwright.sync_api import sync_playwright
from playwright._impl._api_context import PlaywrightContextManager

# This will ensure browser binaries are installed on app startup
def ensure_browsers_installed():
    import subprocess
    try:
        subprocess.run(["playwright", "install", "chromium"], check=True)
    except Exception as e:
        st.error(f"Error installing browsers: {e}")

st.title("Headless Browser Screenshot")

ensure_browsers_installed()  # Install browser binaries if missing

url = st.text_input("Enter URL", "https://example.com")

if st.button("Take Screenshot"):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        screenshot = page.screenshot()
        browser.close()
    st.image(screenshot)
