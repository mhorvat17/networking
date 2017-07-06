from napalm_base import get_network_driver
import re
import csv
import numpy as np
import urllib
import base64
from modules.fn_get_bgp_neighbors import fn_get_bgp_neighbors
from modules.fn_get_facts import fn_get_facts
from modules.fn_traceroute import fn_traceroute
devices = np.genfromtxt('devices.csv',delimiter=",",dtype=str)
answer = input("Do you want to: \n 1. Get the Device Facts \n 2. Get the Device BGP neighbors \n 3. Traceroute from device \n")
if answer == '3':
    destination == input('Which IP address would you like to traceroute to? \n')
    timeout == '2'
    vrf == input('Which VRF would you like to traceroute from? \n')

for creds in devices[1:]:
  password = base64.b64decode(creds[3])
  if answer == '1':
    print ("Getting your device facts for " + creds[0])
    fn_get_facts(creds[0],creds[1],creds[2],password)
  if answer == '2':
      print ("Getting your device bgp neighbors for " + creds[0])
      fn_get_bgp_neighbors(creds[0],creds[1],creds[2],password)
  if answer == '3':
      traceroute = input("Do you want to traceroute from " + creds[0] + "? [y/n]")
      if traeroute == 'y':
        fn_traceroute(creds[0],creds[1],creds[2],password,destination,timeout,vrf)
