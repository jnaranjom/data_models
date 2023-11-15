""" Function to validate IP addresses on data models """

from netaddr import *
import yaml

models = ['aaa', 'dns', 'syslog']

for model in models:
    with open("config_contexts/" + model + ".yml", 'r') as data_model:
        data_model = yaml.safe_load(data_model)
    try:
        for address in data_model[model]['servers']:
            result = IPAddress(address['ip'])
            assert str(address['ip']) == str(result)
    except:
        print(f"IP address validation failed for: {model.upper()} IP: {str(address['ip'])}")

print ("No Validation errors found.")
