'''
Functions : function.py
system configuration : config.py
'''


import sys
sys.path.append('../Libraries_Pkg')
from functions import *


#test_ListExhistingSanpshots()
print ("****************************************************Creating   Snapshot****************************************************")

# Variables
Snapshot_ID = ""
volId_List=[]
url =  base_url + "/snapshots"
Sanpshot_Name = "Aaftab_Automation"
Cutover_Flag = False


Snapshot_ID, volId_List = create_snap_func(url, Sanpshot_Name, Cutover_Flag)
print("Snapshot created for the following volumes:\n", volId_List)
print("Snapshpt Id:" + str(Snapshot_ID))


"""print ("****************************************************Create Snapshot End****************************************************")


print ("****************************************************Attaching Volumes****************************************************")
#d_open(instance_id, SnapId, volIds)
print ("****************************************************Attached Volumes****************************************************")

snapshots = get_exhistingSnapshotList(url)
print (snapshots)
"""