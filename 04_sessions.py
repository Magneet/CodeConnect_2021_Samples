inventory=vmware_horizon.Inventory(url=hvconnectionobj.url, access_token=hvconnectionobj.access_token)
sessions = inventory.get_sessions()
print(sessions[0])
id = sessions[0].get('id')


filter = {}
filter["type"] = "And"
filter["filters"] = []
filter1={}

filter1["type"] = "Equals"
filter1["name"] = "session_state"
filter1["value"] = "DISCONNECTED"

filter["filters"].append(filter1)

sessions = inventory.get_sessions(filter=filter)
for i in sessions:
    for ii in i:
        print(ii, '=', i[ii] )


session_ids = []
for i in sessions:
    session_ids.append(i.get('id'))

inventory.send_message_sessions(session_ids=ids, message = "This is an informational message during CodeConnect" )
inventory.send_message_sessions(session_ids=ids, message = "This is an Error message during CodeConnect",message_type = "ERROR")

inventory.restart_session_machines(session_ids=session_ids)
inventory.reset_session_machines(session_ids=session_ids)
inventory.logoff_sessions(session_ids=session_ids)