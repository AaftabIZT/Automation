'''
prerequisite : All VM's setup and configured,
               Swagger server up and running,
               driver installed with cbt enabled.
Functions : function.py
system configuration : config.py

NOTE : SCRIPT FOR VALID TEST CASE
'''
import time
import sys
sys.path.append('../Libraries_Pkg')
from functions import *

# Variables
snapShotNameFULL = 'Aaftab_Automation_1'                   # Please provide your SnapShot Name
url =  base_url + "/snapshots"
snapShotNameINCR  = "Aaftab_Automation_2"
Cutover_Flag = False
vol_ID = "vol-0e5006b60432bfa8d"

"""
Snapshot_ID_1, volId_List = create_snap_func(url, snapShotNameFULL, Cutover_Flag)
print("Snapshpt Id_2:" + str(Snapshot_ID_1))

time.sleep(50)

Snapshot_ID_2, volId_List = create_snap_func(url, snapShotNameINCR, Cutover_Flag)
print("Snapshpt Id_2:" + str(Snapshot_ID_2))

"""


Snapshot_ID_1 = "c5210bca-918b-11e8-a166-02f0edaa3348"
Snapshot_ID_2 = "60d53e92-9191-11e8-ab92-02f0edaa3348"

url = base_url + "/cbt/disk-changed-areas"
print(url)

#Order of snapshots (Incremental snapshot first then Full snapshot)
response = query_Changes(url, Snapshot_ID_2, Snapshot_ID_1, vol_ID, 0)
print(response)

