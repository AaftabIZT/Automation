#Author-Sulom Tulshibagwale
#Created On- Jul 10 12:59 IST 2018

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.drivers import ec2
import sys
import paramiko

sys.path.append('../Libraries_Pkg')
from functions import *

BASE_DRIVER = get_driver(Provider.EC2)
EC2_DRIVER = BASE_DRIVER(AccessKey_, \
                         SecretKey_, \
                         region=Region_)

SnapId=""
volIds=[]



def getInstance(Cloud_Handle, szInstanceID):
    if 0 >= len(szInstanceID):
        return None

    list_str = []
    list_str.append(szInstanceID)

    list_instance = Cloud_Handle.list_nodes(list_str)

    if 0 is len(list_instance):
        return None

    else:
        return list_instance[0]

###Take full snapshot
print ("****************************************************Creating   Snapshot Cutover False****************************************************")
Snapshot_Name="Test_False_Automation"
Cutover_Flag=False
url = base_url + instance_id + "/snapshots"
SnapId_F, volIds_F = create_snap_func(url, Snapshot_Name, Cutover_Flag)
print("Snapshot created for the following volumes:\n", volIds_F)
print("Snapshpt Id:" + str(SnapId))

print ("****************************************************Create Snapshot End****************************************************")

print ("****************************************************Attaching Volumes****************************************************")

disks_full = d_open(instance_id, SnapId_F, volIds_F)
print(disks_full)

print ("****************************************************Attached Volumes****************************************************")
'''
###Write Data to Guest Machine

print("Instance used for testing is :: " + INSTANCE_ID)
# Consider the instance as input and driver ready.
# Take the node object to get the list of volumes.
nodes = EC2_DRIVER.list_nodes()
nodeObj = ""
for node in nodes:
    if node.id == INSTANCE_ID:
        nodeObj = node
instance_obj = getInstance(EC2_DRIVER, INSTANCE_ID)
print(instance_obj)
PLATFORM = instance_obj.extra['platform']
print(PLATFORM)

if PLATFORM == 'windows':
    #write data using winscp
    pass

else:
    #use ssh and cli for data writing.
    pass'''


###Take incremental snapshot
print ("****************************************************Creating   Snapshot Cutover False****************************************************")
Snapshot_Name="Test_True_Automation"
Cutover_Flag=True
url = base_url + instance_id + "/snapshots"
SnapId_T, volIds_T = create_snap_func(url, Snapshot_Name, Cutover_Flag)
print("Snapshot created for the following volumes:\n", volIds_T)
print("Snapshpt Id:" + str(SnapId))

print ("****************************************************Create Snapshot End****************************************************")

print ("****************************************************Attaching Volumes****************************************************")

disks_incr = d_open(instance_id, SnapId_T, volIds_T)
print(disks_incr)

print ("****************************************************Attached Volumes****************************************************")


'''
###ssh to CVM for data verification
hostname = '18.130.59.250'
myuser   = 'centos'
mySSHK   = '/home/sulom/Sulom-WindowsGuest.pem'
sshcon   = paramiko.SSHClient()
sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshcon.connect(hostname, username=myuser, key_filename=mySSHK)'''

for vol in volIds_F:
    full = disks_full[vol]
    incr = disks_incr[vol]
    print("Full Disk for vol:",vol,full)
    print("Incr Disk for vol:", vol, incr)

#List files on home to enshure ssh connection
#stdin, stdout, stderr = sshcon.exec_command("ls -l ")
#print (stdout.read())

