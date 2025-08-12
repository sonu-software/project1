import streamlit as st
import requests
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="Text-to-Image Generator", layout="centered")
st.title("🎨 Text-to-Image Generator (SDXL via Hugging Face)")

# Hugging Face model to use
MODEL = "stabilityai/stable-diffusion-xl-base-1.0"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
headers = {
    "Authorization": f"Bearer {st.secrets['hf_token']}"
}

def generate_image(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        st.error(f"Failed to generate image. Status code: {response.status_code}")
        st.error(response.text)
        return None
    
    return Image.open(BytesIO(response.content))

# UI
prompt = st.text_input("Enter your image prompt", "A cyberpunk city at night, neon lights, rainy street")

if st.button("Generate Image"):
    with st.spinner("Generating image... please wait"):
        img = generate_image(prompt)
        if img:
            st.image(img, caption=prompt, use_column_width=True)
