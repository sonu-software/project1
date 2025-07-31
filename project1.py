import os
import subprocess
import time
import streamlit as st

from PIL import Image


command1 = 'powershell -command "Add-Type -AssemblyName System.Windows.Forms; Add-Type -AssemblyName System.Drawing; $bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds; $bitmap = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height; $graphics = [System.Drawing.Graphics]::FromImage($bitmap); $graphics.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, $bounds.Size); $bitmap.Save(\'screenshot.png\'); $graphics.Dispose(); $bitmap.Dispose();"'

st.title("cmd run on web")

def take_screenshot():
    #os.system(command1)
    file1=os.system("python take_screenshot.py")

    time.sleep(5) 
    st.success("done")
    st.image("file1", caption="Here is the PNG image", use_container_width=True)

if st.button("Take Screenshot"):
    os.system(command1)  # Make sure this script saves screenshot.png
    time.sleep(5)  # Wait for the screenshot to be saved
    if os.path.exists("screenshot.png"):
        st.success("Screenshot taken!")
        try:
            img = Image.open("screenshot.png")
            st.image(img, caption="Here is the PNG image", use_container_width=True)
        except Exception as e:
            st.error(f"Failed to load image: {e}")
    else:
        st.error("Screenshot failed. File not found.")


if st.button("press this"):
    os.system("netsh wlan show all > output2.txt")
    
    time.sleep(5)

if __name__=="__main__":
    take_screenshot()







