import requests
import json
import datetime
import threading
import time

'''instance_id = "<Guest VM instance id>"
CVM_IP = "<Control VM public ip>"
Region_ = "<Specify your Region>"
SecretKey_ = "<AWS Secret Key>"
AccessKey_ = "<AWS AccessKey>"'''

instance_id = "i-0380596e10d91fb42"
CVM_IP = "18.130.59.250"
Region_ = "eu-west-2"
SecretKey_ = "g5b1/NoUFQWYJob+w0C/6csbAqd04aPWXwmM4lsQ"
AccessKey_  = "AKIAI7HRBSRFPXZA3HQQ"

base_url = "https://"+CVM_IP+":8081/api/"


# Windows guest VM
INSTANCE_ID = "i-0380596e10d91fb42"
INSTANCE_IP = "172.31.18.104"

# Linux guest VM
#INSTANCE_ID = "i-0d0a2abc09a0ad975"
#INSTANCE_IP = "172.31.17.92"