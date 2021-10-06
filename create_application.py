import requests, getpass, urllib, json

import vmware_horizon

requests.packages.urllib3.disable_warnings()
url = "https://pod2cbr1.loft.lab"

# username = input("Username\n")
username = "CodeConnect2021"

# domain = input("Domain\n")
domain = "loft.lab"

pw = getpass.getpass()

hvconnectionobj = vmware_horizon.Connection(username = username,domain = domain,password = pw,url = url)
hvconnectionobj.hv_connect()
print("connected")

monitor = obj=vmware_horizon.Monitor(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
external=vmware_horizon.External(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
inventory=vmware_horizon.Inventory(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
config=vmware_horizon.Config(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)


with open('new_application.json') as f:
    data = json.load(f)

farms = inventory.get_farms()
for i in farms:
    if (i["display_name"]) == "Python_demo_farm":
        farm = i
data["farm_id"] = farm["id"]

del data['anti_affinity_data']
del data['cs_restriction_tags']
del data['desktop_pool_id']


inventory.new_application_pool(application_pool_data=data)

end=hvconnectionobj.hv_disconnect()
print(end)