inventory=vmware_horizon.Inventory(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
machines = inventory.get_machines()
for i in machines:
    for ii in i:
        print(ii, '=', i[ii] )

print(machines[0])
firstmachine = machines[0]
for i in firstmachine:
    print(i, '=', firstmachine[i] )

rds = inventory.get_rds_hosts()
for i in rds:
    print(i.get('name'))