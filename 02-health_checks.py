monitor = vmware_horizon.Monitor(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
print(monitor.connection_servers())
cs = monitor.connection_servers()
for i in cs:
    for ii in i:
        print(ii, '=', i[ii] )

farms = monitor.farms()
for i in farms:
    print(i)

vc = monitor.virtual_centers()
for i in vc:
    for ii in i:
        if ii == "hosts":
            hosts = i[ii]




