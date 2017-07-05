from napalm_base import get_network_driver
import string
import re
import csv
import numpy as np
import webbrowser
import urllib
import base64
from json2html import *
from pprint import pprint


def fn_get_interfaces(hostname,ip,username,password):
   driver = get_network_driver('ios')
   with driver(ip,username,password) as device:
       interfaces = device.get_interfaces()
       interfaces = json2html.convert(json = interfaces)
       return interfaces

def fn_get_facts(hostname,ip,username,password):
       driver = get_network_driver('ios')
       with driver(ip,username,password) as device:
           neighbors = device.get_facts()
           neighbors = json2html.convert(json = neighbors)
           file = open(hostname + '-facts.html', 'w+')
           file.write (neighbors)
           webbrowser.open(hostname + '-facts.html')
           return

def fn_get_bgp_neighbors(hostname,ip,username,password):
       driver = get_network_driver('ios')
       with driver(ip,username,password) as device:
           neighbors = device.get_bgp_neighbors()
           neighbors = json2html.convert(json = neighbors)
           file = open(hostname + '-bgp.html', 'w+')
           file.write (neighbors)
           webbrowser.open(hostname + '-bgp.html')
           return

devices = np.genfromtxt('devices.csv',delimiter=",",dtype=str)
answer = input("Do you want to: \n 1. Get the Device Facts \n 2. Get the Device BGP neighbors \n")
for creds in devices[1:]:
  password = base64.b64decode(creds[3])
  if answer == '1':
    fn_get_facts(creds[0],creds[1],creds[2],password)
  if answer == '2':
        fn_get_bgp_neighbors(creds[0],creds[1],creds[2],password)
