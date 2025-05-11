#!/bin/python/
import os
import time
import requests

def is_build_html_working():
  try:
    reponse = 
requests.get("http://SawyerWetson/SmartUmpires/main/Build.html/
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

      time.sleep(5
  
     
