import requests, getpass, urllib, json, os
os.chdir('D:\GIT\CodeConnect_2021_Samples')

import vmware_horizon

requests.packages.urllib3.disable_warnings()
# url = input("URL\n")
url = "https://pod2cbr1.loft.lab"

# username = input("Username\n")
username = "CodeConnect2021"

# domain = input("Domain\n")
domain = "loft.lab"

pw = getpass.getpass()

hvconnectionobj = vmware_horizon.Connection(username = username,domain = domain,password = pw,url = url)
hvconnectionobj.hv_connect()





