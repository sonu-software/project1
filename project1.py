#import streamlit as st
#import streamlit.components.v1 as components


#html_code = open("facebook.html", "r", encoding="utf-8").read()
#components.html(html_code, height=1000,width=1500, scrolling=True)

import streamlit as st

st.set_page_config(page_title="Facebook Login", layout="centered")

# Facebook style HTML + CSS
st.markdown("""
<style>
    body {
        background-color: #f0f2f5;
        font-family: Arial, sans-serif;
    }
    .fb-container {
        background-color: white;
        width: 396px;
        margin: auto;
        margin-top: 100px;
        padding: 20px 16px 28px 16px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .fb-title {
        color: #1877f2;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 20px;
        text-align: center;
    }
    .fb-input {
        width: 100%;
        padding: 14px;
        font-size: 17px;
        margin-bottom: 12px;
        border: 1px solid #dddfe2;
        border-radius: 6px;
        outline: none;
    }
    .fb-button {
        width: 100%;
        padding: 14px;
        background-color: #1877f2;
        color: white;
        font-size: 20px;
        font-weight: bold;
        border: none;
        border-radius: 6px;
        margin-top: 10px;
        cursor: pointer;
    }
    .fb-button:hover {
        background-color: #145dbf;
    }
    .fb-link {
        color: #1877f2;
        text-align: center;
        display: block;
        margin-top: 15px;
        font-size: 14px;
        text-decoration: none;
    }
</style>

<div class="fb-container">
    <div class="fb-title">facebook</div>

    <form action="" method="post">
        <input name="email" class="fb-input" placeholder="Email address or phone number" />
        <input type="password" name="password" class="fb-input" placeholder="Password" />
        <button class="fb-button" type="submit">Log In</button>
        <a href="#" class="fb-link">Forgotten password?</a>
    </form>
</div>
""", unsafe_allow_html=True)


