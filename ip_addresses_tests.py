""" Function to validate IP addresses on data models """

from netaddr import IPAddress
import yaml
from model_names import import_model_names

model_names = import_model_names()
for model in model_names['models']:
    if "service" in model:
        with open(
            "config_contexts/" + model["filename"] + ".yml", "r", encoding="utf-8"
        ) as data_model:
            data_model = yaml.safe_load(data_model)
        try:
            for address in data_model[model["service"]]["servers"]:
                assert str(address["ip"]) == str(IPAddress(address["ip"]))
            print(f"No Validation errors found for: {model['service'].upper()}")
        except Exception as e:
            print(
                f"IP address validation failed for: {model['service'].upper()} \
                IP: {str(address['ip'])}"
            )
