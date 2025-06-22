#!/bin/python
import os
import time
import requests

def is_setup_py_working():
  try:
    reponse = 
requests.get("https:/SawyerWetson/SmartUmpires/main/src/setup.py/"
       return response.status_code == 200
      except requests.exceptions.RequestException:
       return False:




While True:
 if is_build_html_working():
  print("Build.html is Working. Checking Again in 10 seconds.....")
   time.sleep(10)
  else:
      print("Build.html is not working Rebooting....")
      os.system("git reset -- hard && git pull SawyerWetson/SmartUmpires")
      os.system("start Build.html")

      time.sleep(5)
  
     
