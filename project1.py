# app.py
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import textwrap

st.title("Text-to-Image Generator (Mock)")

prompt = st.text_input("Enter your prompt", "A cute cat sitting on the moon.")

if st.button("Generate Image"):
    # Create a blank image
    img = Image.new("RGB", (512, 512), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Wrap the prompt text
    wrapper = textwrap.TextWrapper(width=40)
    wrapped_text = wrapper.fill(text=prompt)

    # Use a default font
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()

    # Draw the prompt text onto the image
    draw.text((10, 10), wrapped_text, fill="black", font=font)

    st.image(img, caption="Generated image from prompt")
