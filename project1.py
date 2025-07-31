import streamlit as st

st.title("Web-Based Screenshot & Text Viewer (Streamlit Cloud Compatible)")

# Section 1: Upload an image (simulating screenshot)
st.header("📸 Upload a Screenshot")

uploaded_image = st.file_uploader("Upload an image (screenshot)", type=["png", "jpg", "jpeg"])
if uploaded_image:
    st.image(uploaded_image, caption="Your uploaded screenshot", use_container_width=True)

# Section 2: Upload a text file (simulating netsh output)
st.header("📄 Upload Command Output (Text File)")

uploaded_text = st.file_uploader("Upload a text file (e.g., netsh output)", type=["txt"])
if uploaded_text:
    content = uploaded_text.read().decode("utf-8")
    st.text_area("Command Output", content, height=400)
