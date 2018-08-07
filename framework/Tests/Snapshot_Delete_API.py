'''
prerequisite : All VM's setup and configured,
               Swagger server up and running,
               driver installed with cbt enabled
               Snapshot created previously

Functions : function.py
system configuration : config.py

NOTE : SCRIPT FOR VALID TEST CASE
'''

import sys
sys.path.append('../Libraries_Pkg')
from functions import *


snapShotName = 'Aaftab_Automation'                   # Please provide your SnapShot Name
url = base_url + "/snapshots"

snapShotID = get_snapshotInfo(url, snapShotName)

if snapShotID !=None:
    url = base_url + "/snapshot/" + snapShotID
    response = delete_snapShot(url)
    print(response)
else:
    print("Snapshot Name not found")