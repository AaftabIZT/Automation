#Author-Sulom Tulshibagwale
#Created On- Jul 09 12:50 IST 2018

import requests
import json
import datetime
from framework.config import *

Snapshot_ID = ""
volId_List=[]
RespCode = 0
volume_disk = {}


def get_exhistingsnapshotList(url):
    payload = {
        "CloudProvider": "AWS",
        "AwsCreds":
            {
                "Region": Region_,
                "SecretKey": SecretKey_,
                "AccessKey": AccessKey_
            },
        "EsxCreds":
            {
                "IPorFQDN": "",
                "Username": "",
                "Password": ""
            }
    }
    headers = {'content-type': 'application/json'}

    response = requests.request("POST", url, data=json.dumps(payload), \
                            headers=headers,verify=False)
    return str(response.text)

def create_snap_func(url, snapName,Cutover_):
    global Snapshot_ID
    global volId_List
    global RespCode

    payload = {
        "SnapshotName": snapName,
        "Cutover": Cutover_,
        "Tags": [
            {"Key": "Name",
             "Value": snapName
             },

        ],
        "GenericRequest":
            {
                "CloudProvider": "AWS",
                "AwsCreds":
                    {
                        "Region": Region_,
                        "SecretKey": SecretKey_,
                        "AccessKey": AccessKey_
                    },
                "EsxCreds":
                    {
                        "IPorFQDN": "",
                        "Username": "",
                        "Password": ""
                    }
            }
    }

    headers = {'content-type': 'application/json'}
    print(datetime.datetime.now())
    response = requests.request("PUT", url, data=json.dumps(payload), headers=headers, verify=False)

    print(datetime.datetime.now())
    print("Reason is " + str(response.reason))
    print("Status code is " + str(response.status_code))
    print("Response is " + str(response.text))
    RespCode = response.status_code
    if RespCode != 201:
        print  ("CREATE SNAPSHOT FAILED.........")
        return

    resp = json.loads(response.text)
    Snapshot_ID = resp['SnapshotID']
    volId_List = resp['DiskIds']
    return Snapshot_ID,volId_List

def disk_open(instance_id, snapshot_id, volume_iD):
    global volume_disk
    url = base_url+ instance_id + "/snapshot/" + snapshot_id + "/" + volume_iD + "/connection"
    Name_ = "vol_"+volume_iD
    print(url)
    payload = {
        "CloudProvider": "AWS",
        "AwsCreds":
            {
                "Region": Region_,
                "SecretKey": SecretKey_,
                "AccessKey": AccessKey_
            },
        "EsxCreds":
            {
                "IPorFQDN": "",
                "Username": "",
                "Password": ""
            },

    }
    print(payload)
    headers = {'content-type': 'application/json'}
    print(headers)
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)

    print("Reason is " + str(response.reason))
    print("Status code is " + str(response.status_code))
    print("Response is " + str(response.text))
    resp = json.loads(response.text)
    #print "Response................."
    #print resp
    #print (resp['Device'])
    volume_disk[volume_iD] = resp['Device']








def d_open(instance_id, Snapshot_ID, volId_List):
    # Create new threads
    thread_List=[]
    for i in range(0,len(volId_List)):
        thread_List.append(threading.Thread(target=disk_open, args=(instance_id, Snapshot_ID, volId_List[i])))

    for thread in thread_List:
        # Start new Threads
        thread.start()

        time.sleep(20)

    for thread in thread_List:
        # Start new Threads
        thread.join()
    print ("Fetching List of Volumes and the device where the volume made from the Snapshot is attached")
    print (volume_disk)
