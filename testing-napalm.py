from napalm_base import get_network_driver
import re
import csv
import numpy as np
import urllib
import base64
from modules.fn_get_bgp_neighbors import fn_get_bgp_neighbors
from modules.fn_get_facts import fn_get_facts
devices = np.genfromtxt('devices.csv',delimiter=",",dtype=str)
answer = input("Do you want to: \n 1. Get the Device Facts \n 2. Get the Device BGP neighbors \n")
for creds in devices[1:]:
  password = base64.b64decode(creds[3])
  if answer == '1':
    fn_get_facts(creds[0],creds[1],creds[2],password)
  if answer == '2':
        fn_get_bgp_neighbors(creds[0],creds[1],creds[2],password)
