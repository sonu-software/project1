#import streamlit as st
#import streamlit.components.v1 as components


#html_code = open("facebook.html", "r", encoding="utf-8").read()
#components.html(html_code, height=1000,width=1500, scrolling=True)

import streamlit as st
import streamlit.components.v1 as components

# Load the combined Facebook-style CSS (from your zip)
css_paths = [
    "/mnt/data/login_files/login_files/-8trMzOyqMx.css",
    "/mnt/data/login_files/login_files/45aoXJzAiH9.css",
    "/mnt/data/login_files/login_files/tWqglhf7NaO.css"
]

combined_css = ""
for path in css_paths:
    with open(path, "r", encoding="utf-8", errors="ignore") as file:
        combined_css += file.read() + "\n\n"

# Sample Facebook-like login HTML
html_content = f"""
<html>
<head>
    <style>
        {combined_css}
        body {{
            background-color: #f0f2f5;
            font-family: Helvetica, Arial, sans-serif;
        }}
        .login-container {{
            width: 360px;
            margin: 100px auto;
            padding: 40px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }}
        .login-title {{
            color: #1877f2;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 24px;
            text-align: center;
        }}
        .login-input {{
            width: 100%;
            padding: 12px;
            margin-bottom: 14px;
            border: 1px solid #ccc;
            border-radius: 6px;
            font-size: 16px;
        }}
        .login-button {{
            width: 100%;
            padding: 12px;
            background-color: #1877f2;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }}
        .login-button:hover {{
            background-color: #145dbf;
        }}
        .login-link {{
            text-align: center;
            margin-top: 12px;
        }}
        .login-link a {{
            color: #1877f2;
            font-size: 14px;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <div class="login-container">
        <div class="login-title">facebook</div>
        <form>
            <input type="text" class="login-input" placeholder="Email address or phone number" />
            <input type="password" class="login-input" placeholder="Password" />
            <button type="submit" class="login-button">Log In</button>
        </form>
        <div class="login-link"><a href="#">Forgotten password?</a></div>
    </div>
</body>
</html>
"""

# Display inside Streamlit
components.html(html_content, height=700, scrolling=False)

