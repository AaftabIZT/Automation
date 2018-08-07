'''
Functions : function.py
system configuration : config.py

NOTE : SCRIPT FOR VALID TEST CASE

prerequisite : All VM's setup and configured,
               Swagger server up and running,
               driver installed with cbt enabled.
'''


import threading

import sys
sys.path.append('../Libraries_Pkg')
from functions import *


# Variables
# Snapshot_ID = ""
# volId_List=[]
url =  base_url + "/snapshots"               # change instanceID for Invalid testcase from config.py
Sanpshot_Name = "Aaftab_Automation"          # Please provide Snapshot Name
Cutover_Flag = False


print(url)


"""t1 = threading.Thread(target=create_snap_func, args=(url,Sanpshot_Name,Cutover_Flag))
t2 = threading.Thread(target=create_snap_func, args=(url,Sanpshot_Name,Cutover_Flag))

t1.start()
t2.start()

t1.join()
t2.join()
"""

Snapshot_ID, volId_List = create_snap_func(url, Sanpshot_Name, Cutover_Flag)
#print("Snapshot created for the following volumes:\n", volId_List)
#print("Snapshpt Id:" + str(Snapshot_ID))