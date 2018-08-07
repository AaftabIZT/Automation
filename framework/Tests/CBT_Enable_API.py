'''
prerequisite : All VM's setup and configured,
               Swagger server up and running,

Functions : function.py
system configuration : config.py

NOTE : SCRIPT FOR VALID TEST CASE
'''


import sys
sys.path.append('../Libraries_Pkg')
from functions import *


url = base_url + "/cbt"
response = enable_CBT(url)
print(response)

