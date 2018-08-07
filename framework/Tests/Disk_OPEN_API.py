'''
Functions : function.py
system configuration : config.py
prerequisite : All VM's setup and configured,
               Swagger server up and running,
               driver installed with cbt enabled
               Snapshot created for specified volume.

NOTE : SCRIPT FOR VALID TEST CASE
'''

import threading

lock_val = threading.Lock()

import sys
sys.path.append('../Libraries_Pkg')
from functions import *


snapshotID = "9b61977e-9577-11e8-bc31-02f0edaa3348"
volID = "vol-08fc370a620b8a333"

volID_2 = "vol-0e5006b60432bfa8d"
volID_3 = "vol-0731ccf8d3af4cdfb"
volID_4 = "vol-0dc622bf2191ecc7d"
volID_5 = "vol-071d2ff1a20449ac2"
volID_6 = "vol-05d6ea06396e1c341"
volID_7 = "vol-0081a420d861203f4"
volID_8 = "vol-07bb371208a087457"
volID_9 = "vol-0a7649a69d3bd8b88"
volID_10 = "vol-02409c4d044df9fdb"

# args = instance ID, Snapshot ID, Volume ID
LIN_UVM_2_t1  = threading.Thread(target=disk_open, args=(snapshotID,volID))

#LIN_UVM_2_t2 = threading.Thread(target=disk_open,args=(snapshotID,volID_2))
#LIN_UVM_2_t3 = threading.Thread(target=disk_open,args=(snapshotID,volID_3))
#LIN_UVM_2_t4 = threading.Thread(target=disk_open,args=(snapshotID,volID_4))
#LIN_UVM_2_t5 = threading.Thread(target=disk_open,args=(snapshotID,volID_5))
#LIN_UVM_2_t6 = threading.Thread(target=disk_open,args=(snapshotID,volID_6))
#LIN_UVM_2_t7 = threading.Thread(target=disk_open,args=(snapshotID,volID_7))
#LIN_UVM_2_t8 = threading.Thread(target=disk_open,args=(snapshotID,volID_8))
#LIN_UVM_2_t9 = threading.Thread(target=disk_open,args=(snapshotID,volID_9))
#LIN_UVM_2_t10 = threading.Thread(target=disk_open,args=(snapshotID,volID_10))

LIN_UVM_2_t1.start()

#LIN_UVM_2_t2.start()
#LIN_UVM_2_t3.start()
#LIN_UVM_2_t4.start()
#LIN_UVM_2_t5.start()
#LIN_UVM_2_t6.start()
#LIN_UVM_2_t7.start()
#LIN_UVM_2_t8.start()
#LIN_UVM_2_t9.start()
#LIN_UVM_2_t10.start()




LIN_UVM_2_t1.join()

#LIN_UVM_2_t2.join()
#LIN_UVM_2_t3.join()
#LIN_UVM_2_t4.join()
#LIN_UVM_2_t5.join()
#LIN_UVM_2_t6.join()
#LIN_UVM_2_t7.join()
#LIN_UVM_2_t8.join()
#LIN_UVM_2_t9.join()
#LIN_UVM_2_t10.join()


#cid = "8596df5c-90af-11e8-b88d-02f0edaa3348"