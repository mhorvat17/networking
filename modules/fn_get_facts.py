def fn_get_facts(hostname,ip,username,password):
       driver = get_network_driver('ios')
       with driver(ip,username,password) as device:
           neighbors = device.get_facts()
           neighbors = json2html.convert(json = neighbors)
           file = open(hostname + '-facts.html', 'w+')
           file.write (neighbors)
           webbrowser.open(hostname + '-facts.html')
           return
