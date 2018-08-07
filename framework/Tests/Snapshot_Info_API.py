'''
prerequisite : All VM's setup and configured,
               Swagger server up and running,
               driver installed with cbt enabled
Functions : function.py
system configuration : config.py

'''

import sys
sys.path.append('../Libraries_Pkg')
from functions import *


snapShotName = 'Aaftab_Automation'                   # Please provide your SnapShot Name
url = base_url + "/snapshots"

snapShotID = get_snapshotInfo(url, snapShotName)


if snapShotID != None:
    url = base_url + "/snapshot/" + snapShotID
    snapshotsinfo = get_exhistingSnapshotList(url)
    print(snapshotsinfo)
else:
    print("Snapsnot name not found")