#import streamlit as st
#import streamlit.components.v1 as components


#html_code = open("facebook.html", "r", encoding="utf-8").read()
#components.html(html_code, height=1000,width=1500, scrolling=True)

import streamlit as st

st.set_page_config(page_title="Facebook Login", layout="centered")

# Inject CSS to mimic Facebook style
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f5;
        }
        div[data-testid="stVerticalBlock"] {
            margin-top: 100px;
        }
        .stTextInput > div > div > input {
            padding: 14px;
            font-size: 17px;
            border-radius: 6px;
        }
        .stTextInput label {
            display: none;
        }
        .stButton button {
            background-color: #1877f2;
            color: white;
            font-size: 20px;
            font-weight: bold;
            border: none;
            padding: 12px;
            border-radius: 6px;
            width: 100%;
            margin-top: 10px;
        }
        .stButton button:hover {
            background-color: #145dbf;
        }
        .title {
            color: #1877f2;
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
            font-family: Arial, sans-serif;
        }
        .forgot {
            text-align: center;
            margin-top: 12px;
        }
        .forgot a {
            color: #1877f2;
            text-decoration: none;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# UI Layout
st.markdown('<div class="title">facebook</div>', unsafe_allow_html=True)
email = st.text_input("Email", placeholder="Email address or phone number")
password = st.text_input("Password", type="password", placeholder="Password")
login = st.button("Log In")

if login:
    st.success("Login submitted!")
    st.write("📧 Email:", email)
    st.write("🔑 Password:", password)

st.markdown('<div class="forgot"><a href="#">Forgotten password?</a></div>', unsafe_allow_html=True)
