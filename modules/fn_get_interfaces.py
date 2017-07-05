def fn_get_interfaces(hostname,ip,username,password):
   driver = get_network_driver('ios')
   with driver(ip,username,password) as device:
       interfaces = device.get_interfaces()
       interfaces = json2html.convert(json = interfaces)
       return
