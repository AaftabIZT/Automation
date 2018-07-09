#Author-Sulom Tulshibagwale
#Created On- Jul 09 12:50 IST 2018
import requests
import json
import datetime
from framework.config import *


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
