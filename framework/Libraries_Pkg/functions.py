# Author- Aaftabullah Khwaja
# Created On- Jul 09 12:50 IST 2018

import sys
import requests
import json
import datetime
import threading
import time

sys.path.append('../')
from config import *

Snapshot_ID = ""
volId_List=[]
RespCode = 0
volume_disk = {}

requests.packages.urllib3.disable_warnings()            # WARNINGS ARE DISABLED, COMMENT IF NOT NEEDED

def get_exhistingSnapshotList(url):
    '''
    :param : Snapshot api (base_url/snapshots)
    :return : List of snapshot info
    '''
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
    print("Response code for list of existing snapshots " + str(response.status_code))

    return str(response.text)


def create_snap_func(url, snapName, Cutover_):
    """
    :param url: URL for create snapshot call (base_url/snapshots)
    :param snapName: Name for snapshot creation
    :param Cutover_: Value for cutover (True/false)
    :return: Response for create snapshot API
    """
    global Snapshot_ID
    global volId_List
    global RespCode

    payload = {
        "SnapshotName": snapName,
        "Cutover": Cutover_,
        "Tags": [
            {"Key": "Name",
             "Value": snapName
            }

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
    response = requests.request("PUT", url, data=json.dumps(payload), headers=headers, verify=False, timeout=18000)

    print(datetime.datetime.now())
    print("Status is " + str(response.reason))
    print("Status code is " + str(response.status_code))
    print("Response is " + str(response.text))
    RespCode = response.status_code
    if RespCode != 201:
        print("CREATE SNAPSHOT FAILED.........")
        return

    resp = json.loads(response.text)
    Snapshot_ID = resp['SnapshotID']
    volId_List = resp['DiskIds']
    return Snapshot_ID,volId_List


def get_snapshotInfo(url, snapShotName):
    """
    :param url: URL for get snapshot info (base_url/snapshots)
    :param snapShotName: Snapshot name for which info is required
    :return: snapShotID
    """
    response = get_exhistingSnapshotList(url)
    resp_list = list(json.loads(response))
    for element in resp_list:
        if element['SnapshotName'] == snapShotName:
            return element['SnapshotID']
    return None


def delete_snapShot(url):
    """
    :param url: url for snapshot deletion (base_url/snapshot/snapShotID)
    :return: delete API response
    """
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

    response = requests.request("DELETE", url, data=json.dumps(payload), headers=headers, verify=False)
    print("Response code for Delete Snapshot" + str(response.status_code))
    return str(response.text)


def enable_CBT(url):
    """
    :param url: URL for enable CBT (base_url/cbt)
    :return: Response of Enable CBT driver
    """
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

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)
    print("Response code for Enable CBT " + str(response.status_code))
    return str(response.text)


def disable_CBT(url):
    """
    :param url: URL for enable CBT (base_url/cbt)
    :return: Response of Disable CBT driver
    """
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

    response = requests.request("DELETE", url, data=json.dumps(payload), headers=headers, verify=False)
    print("Response code for Disable CBT " + str(response.status_code))
    return str(response.text)


def cbt_Info(url):
    """
    :param url: URL for enable CBT (base_url/cbt)
    :return: API response
    """
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

    response = requests.request("GET", url, data=json.dumps(payload), headers=headers, verify=False)

    print("Response code for CBT Info " + str(response.status_code))
    return str(response.text)


def query_Changes(url, SnapShot_1, SnapShot_2, vol_ID, offset=0):
    """
    :param url: URL for query changes (base_url/cbt/disk-changed-areas)
    :param SnapShot_1: Incremental snapshot ID
    :param SnapShot_2: Full snapshot ID
    :param vol_ID: Volume ID for which Snapshots are taken
    :param offset: Start offset value
    :return: API response
    """
    payload = {
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
            },

        "SnapshotID": SnapShot_1,
        "PrevSnapshotID": SnapShot_2,
        "DiskID": vol_ID,
        "StartOffset": offset
    }

    headers = {'content-type': 'application/json'}

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)
    print("Response code for Query change is",response.status_code)
    return response.text


def disk_open(snapshot_id, volume_id):
    """
    :param instance_id: Guest VM instance ID
    :param snapshot_id: Snapshot ID for which volume is to be attached to Control VM
    :param volume_iD: Guest VM volume ID from which snapshot is created.
    :return:
    """
    url = base_url + "/snapshot/"+snapshot_id+"/"+volume_id+"/connection"
    print(url)
    payload = {
		"CloudProvider":"AWS",
		"AwsCreds":
		{
			"Region":Region_,
			"SecretKey":SecretKey_,
			"AccessKey":AccessKey_
		},
		"EsxCreds":
		{
			"IPorFQDN": "",
			"Username":"",
			"Password":""
		}
}
    headers = {'content-type': 'application/json'}
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers,verify=False)


    print("Reason is "+str(response.reason))
    print("Status code is "+str(response.status_code))
    print("Response is "+str(response.text))


def disk_close(url):
    """
    :param url: url for disk open (base_url/snapshot/snapshotID/volID/connection/ConnectionID)
    :return: API Response (Connection ID)
    """
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
            }
    }

    headers = {'content-type': 'application/json'}

    response = requests.request("DELETE", url, data=json.dumps(payload), headers=headers, verify=False)

    print("Reason is " + str(response.reason))
    print("Status code is " + str(response.status_code))
    print("Response is " + str(response.text))
    return response

def updateMetaData(url, snapshotName):
    """
    :param url: URL for update Meta data (base_url/snapshot/snapShotID)
    :param snapshotName:  Snapshot name for which Meta data is to be updated
    :return: API response
    """
    payload = {
      "GenericRequest": {
        "AwsCreds": {
          "AccessKey": AccessKey_,
          "Region": Region_,
          "SecretKey": SecretKey_
        },
        "CloudProvider": "AWS",
        "EsxCreds": {
          "IPorFQDN": "",
          "Password": "",
          "Username": ""
        }
      },
      "SnapshotName": snapshotName,
      "Tags": [
        {
          "Key": "Name",
          "Value": "ASDAs"
        },
        {
          "Key": "HKey2",
          "Value": "Test_Mod2"
        }
      ]
    }
    headers = {'content-type': 'application/json'}

    response = requests.request("PATCH", url, data=json.dumps(payload), headers=headers, verify=False)
    #if RespCode != 201:
     #   print("Query failed")
     #   return
    print("Reason is " + str(response.reason))
    print("Status code is " + str(response.status_code))
    print("Response is " + str(response.text))
    return (response)


def get_VMProperties(url):
    """
    :param url: URL for VMProperties (base_url/getVMProperties)
    :return: Response of API
    """
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

    response = requests.request("GET", url, data=json.dumps(payload), \
                                headers=headers, verify=False)

    print("Reason is " + str(response.reason))
    print("Status code is " + str(response.status_code))
    print("Response is " + str(response.text))
    return response
