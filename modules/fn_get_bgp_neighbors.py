def fn_get_bgp_neighbors(hostname,ip,username,password):
       driver = get_network_driver('ios')
       with driver(ip,username,password) as device:
           neighbors = device.get_bgp_neighbors()
           neighbors = json2html.convert(json = neighbors)
           file = open(hostname + '-bgp.html', 'w+')
           file.write (neighbors)
           webbrowser.open(hostname + '-bgp.html')
           return
