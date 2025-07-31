import os
import subprocess
import time
import streamlit as st


command1 = 'powershell -command "Add-Type -AssemblyName System.Windows.Forms; Add-Type -AssemblyName System.Drawing; $bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds; $bitmap = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height; $graphics = [System.Drawing.Graphics]::FromImage($bitmap); $graphics.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, $bounds.Size); $bitmap.Save(\'screenshot.png\'); $graphics.Dispose(); $bitmap.Dispose();"'

st.title("cmd run on web")

def take_screenshot():
    #os.system(command1)
    os.system("python take_screenshot.py")

    time.sleep(5) 
    st.success("done")
    st.image("screenshot.png", caption="Here is the PNG image", use_container_width=True)

if st.button("Take Screenshot"):
    os.system("python take_screenshot.py")  # Make sure this script saves screenshot.png
    time.sleep(5)  # Wait for the screenshot to be saved
    if os.path.exists("screenshot.png"):
        st.success("Screenshot taken!")
        st.image("screenshot.png", caption="Here is the PNG image", use_container_width=True)
    else:
        st.error("Screenshot failed. File not found.")


if st.button("press this"):
    os.system("netsh wlan show all > output2.txt")
    time.sleep(5)

if __name__=="__main__":
    take_screenshot()
    

