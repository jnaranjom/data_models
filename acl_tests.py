""" Function to validate IP addresses on data models """

from netaddr import IPAddress, IPNetwork
import yaml

models = [
    {"service": "mgmt_acl", "filename": "mgmt_acl"},
    {"service": "snmp_acl", "filename": "snmp_acl"}
]

for model in models:
    with open("config_contexts/" + model["filename"] + ".yml", "r") as data_model:
        data_model = yaml.safe_load(data_model)
    try:
        for entry in data_model[model["service"]]["entries"]:
            ## Validate action
            assert entry['action'] in ['permit', 'deny']

            ## Validate Source
            if entry['source'] == 'any' or entry['source'] == 'host':
                assert entry['source'] in ['any', 'host']
            else:
                assert entry['source'] == str(IPNetwork(entry['source']))

            ## Validate Destination
            if entry['destination'] == 'any' or entry['destination'] == 'host':
                assert entry['destination'] in ['any', 'host']
            else:
                assert entry['destination'] == str(IPNetwork(entry['destination']))
        print(f"No Validation errors found for {model['service'].upper()}")
    except:
        print(
            f"ACL validation failed for: {model['service'].upper()}. Entry: {entry}"
        )
