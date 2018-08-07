'''
Functions : function.py
system configuration : config.py
prerequisite : All VM's setup and configured,
               Swagger server up and running,
               driver installed with cbt enabled
               Disk attached to control VM.

NOTE : SCRIPT FOR VALID TEST CASE
'''

import sys
sys.path.append('../Libraries_Pkg')
from functions import *

# url = base_url/snapshot/snapshotID/volID/connection/connectionID


snapshotID = "a3a36a3a-8e55-11e8-b21b-02f0edaa3348"         # Need to modify for independent call
volID = "vol-08fc370a620b8a333"
ConnectionID = "b46702d6-8e56-11e8-8638-02f0edaa3348"

url = base_url + "/snapshot/"+snapshotID+"/"+volID+"/connection/"+ConnectionID

response = disk_close(url)
