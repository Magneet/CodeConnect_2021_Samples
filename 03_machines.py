inventory=vmware_horizon.Inventory(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
machines = inventory.get_machines()
print(json.dumps(machines, indent=2, default=str))

print(machines[0])
firstmachine = machines[0]
print(json.dumps(machines, indent=2, default=str))

rds = inventory.get_rds_servers()
print(json.dumps(rds, indent=2, default=str))

machine_ids = []
machine_ids.append((machines[0]).get('id'))

inventory.reset_machines()