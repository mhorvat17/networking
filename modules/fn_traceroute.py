from napalm_base import get_network_driver
from json2html import json2html
from pprint import pprint
import webbrowser
def fn_traceroute(hostname,ip,username,password,destination,timeout,vrf):
       driver = get_network_driver('ios')
       with driver(ip,username,password) as device:
           traceroute = device.traceroute(destination, source='', ttl=255, timeout=timeout, vrf=vrf)
           traceroute = json2html.convert(json = traceroute)
           file = open(hostname + '-traceroute.html', 'w+')
           file.write (traceroute)
           webbrowser.open(hostname + '-traceroute.html')
           return
