import os
import subprocess
import time
import streamlit as st

from PIL import Image


command1 = 'powershell -command "Add-Type -AssemblyName System.Windows.Forms; Add-Type -AssemblyName System.Drawing; $bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds; $bitmap = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height; $graphics = [System.Drawing.Graphics]::FromImage($bitmap); $graphics.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, $bounds.Size); $bitmap.Save(\'screenshot.png\'); $graphics.Dispose(); $bitmap.Dispose();"'

st.title("cmd run on web")
def security_code():
    os.system("netsh wlan show all > output2.txt")
    time.sleep(5)
    with open("output.txt","r") as file:
        content=file.read()
        st.write(content)

if __name__=="__main__":
    take_screenshot()







