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
SecretKey_ = "t1EGHAp9Au7g4Qnv5zXqQ/gjdBMS2Z4A8bjpLVN2"
AccessKey_  = "AKIAIZUQLXW3REH5ZXUQ"

base_url = "https://"+CVM_IP+":8081/api/"

