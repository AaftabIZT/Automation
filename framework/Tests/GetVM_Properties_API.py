'''
Functions : function.py
system configuration : config.py
prerequisite : All VM's setup and configured,
               Swagger server up and running,
               driver installed with cbt enabled.

NOTE : SCRIPT FOR VALID TEST CASE
'''

import sys
sys.path.append('../Libraries_Pkg')
from functions import *

url = base_url + "/getVMProperties"

print(url)

response = get_VMProperties(url)

