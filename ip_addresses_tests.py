""" Function to validate IP addresses on data models """

from netaddr import IPAddress
import yaml

models = [
    {"service": "aaa", "filename": "aaa"},
    {"service": "dns", "filename": "dns"},
    {"service": "syslog", "filename": "syslog"},
    {"service": "ntp", "filename": "ntp_core"},
    {"service": "ntp", "filename": "ntp_edge"},
]

for model in models:
    with open("config_contexts/" + model["filename"] + ".yml", "r") as data_model:
        data_model = yaml.safe_load(data_model)
    try:
        for address in data_model[model["service"]]["servers"]:
            assert str(address["ip"]) == str(IPAddress(address["ip"]))
        print(f"No Validation errors found for: {model['service'].upper()}")
    except:
        print(
            f"IP address validation failed for: {model['service'].upper()} IP: {str(address['ip'])}"
        )
