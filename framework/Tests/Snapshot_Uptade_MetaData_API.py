'''
prerequisite : All VM's setup and configured,
               Swagger server up and running,
               driver installed with cbt enabled
Functions : function.py
system configuration : config.py

NOTE : SCRIPT FOR VALID TEST CASE
'''

import sys
sys.path.append('../Libraries_Pkg')
from functions import *

snapShotName = 'Aaftab_Automation_2'                   # Please provide your SnapShot Name
url = base_url + "/snapshots"

snapShotID = get_snapshotInfo(url, snapShotName)

url = base_url + "/snapshot/" + snapShotID
print(url)

response = updateMetaData(url, "Aaftab_Updated")
