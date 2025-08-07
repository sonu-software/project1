#import streamlit as st
#import streamlit.components.v1 as components


#html_code = open("facebook.html", "r", encoding="utf-8").read()
#components.html(html_code, height=1000,width=1500, scrolling=True)

import streamlit as st

# Custom CSS to style like Facebook
st.markdown("""
    <style>
        .fb-box {
            max-width: 400px;
            margin: 100px auto;
            padding: 40px 30px;
            border: 1px solid #ddd;
            border-radius: 10px;
            background-color: #f0f2f5;
            box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
            font-family: Arial, sans-serif;
        }
        .fb-title {
            color: #1877f2;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
        }
        .fb-input input {
            width: 100%;
            padding: 12px;
            margin: 8px 0 16px;
            border: 1px solid #ccc;
            border-radius: 6px;
            font-size: 16px;
        }
        .fb-button {
            width: 100%;
            padding: 12px;
            background-color: #1877f2;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
        }
        .fb-button:hover {
            background-color: #145dbf;
        }
    </style>
""", unsafe_allow_html=True)

# Create form UI
with st.container():
    st.markdown('<div class="fb-box">', unsafe_allow_html=True)
    st.markdown('<div class="fb-title">facebook</div>', unsafe_allow_html=True)

    email = st.text_input("", placeholder="Email address or phone number")
    password = st.text_input("", type="password", placeholder="Password")

    login = st.button("Log in", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# On login
if login:
    st.success("Login clicked!")
    st.write("📧 Email:", email)
    st.write("🔑 Password:", password)  # Avoid this in real apps!










