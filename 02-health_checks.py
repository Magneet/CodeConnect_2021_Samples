monitor = vmware_horizon.Monitor(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
print(json.dumps(monitor.connection_servers(), indent=2, default=str))
cs = monitor.connection_servers()
print(json.dumps(cs, indent=2, default=str))

farms = monitor.farms()
print(json.dumps(farms, indent=2, default=str))

vc = monitor.virtual_centers()
print(json.dumps(vc, indent=2, default=str))




