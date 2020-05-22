# Name: display_info.py
# Version: 0.3
# Author: Cesar Villegas Ureta - https//www.slayerx.org/
# GitHub repo: https://github.com/cvillegas/python_examples
# License: MIT License
# Description: Mini app to show some info about visitor

import socket 
import time




# Function to display hostname and IP address 
def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 
  



get_Host_name_IP() #Function call 
print('The time is  :', time.ctime())



