help(vmware_horizon)

monitor = vmware_horizon.Monitor(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)

print(dir(monitor))
help(monitor)
help(monitor.connection_servers)