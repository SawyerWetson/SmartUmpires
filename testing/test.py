#!/usr/bin/env python
import os
import time
import requests

def is_setup_py_working():
    try:
        response = requests.get(
            "https://raw.githubusercontent.com/SawyerWetson/SmartUmpires/main/src/setup.py"
        )
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

while True:
    if is_setup_py_working():
        print("setup.py is accessible. Checking again in 10 seconds.....")
        time.sleep(10)
    else:
        print("setup.py is not accessible. Rebooting....")
        os.system("git reset --hard && git pull SawyerWetson main")
        os.system("start setup.py")  # This only works on Windows with proper associations
        time.sleep(5)
