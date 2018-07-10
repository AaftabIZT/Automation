from framework.Libraries_Pkg.Func import *
from framework.config import *


SnapId=""
volIds=[]

def test_ListExhistingSanpshots():
    url = base_url + instance_id + "/snapshots"
    snapshots = get_exhistingsnapshotList(url)
    print (snapshots)

def test_CreateSnapShot1():
    global SnapId
    global volIds
    Sanpshot_Name="Test_False_Automation"
    Cutover_Flag=False
    url = base_url + instance_id + "/snapshots"
    SnapId,volIds = create_snap_func(url,Sanpshot_Name,Cutover_Flag)
    print ("Snapshot created for the following volumes:\n",volIds)
    print ("Snapshpt Id:"+str(SnapId))


#test_ListExhistingSanpshots()

print ("****************************************************Creating   Snapshot****************************************************")
test_CreateSnapShot1()
print ("****************************************************Create Snapshot End****************************************************")


print ("****************************************************Attaching Volumes****************************************************")
d_open(instance_id, SnapId, volIds)
print ("****************************************************Attached Volumes****************************************************")

