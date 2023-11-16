""" Function to validate IP addresses on data models """

from netaddr import IPNetwork
import yaml
from model_names import import_model_names

model_names = import_model_names()
for model in model_names['models']:
    if "acl" in model:
        with open(
            "config_contexts/" + model["filename"] + ".yml", "r", encoding="utf-8"
        ) as data_model:
            data_model = yaml.safe_load(data_model)
        try:
            for entry in data_model[model["acl"]]["entries"]:
                ## Validate action
                assert entry["action"] in ["permit", "deny"]

                ## Validate Source
                if entry["source"] == "any" or entry["source"] == "host":
                    assert entry["source"] in ["any", "host"]
                else:
                    assert entry["source"] == str(IPNetwork(entry["source"]))

                ## Validate Destination
                if entry["destination"] == "any" or entry["destination"] == "host":
                    assert entry["destination"] in ["any", "host"]
                else:
                    assert entry["destination"] == str(IPNetwork(entry["destination"]))
            print(f"No Validation errors found for {model['acl'].upper()}")
        except Exception as e:
            print(f"ACL validation failed for: {model['acl'].upper()}. Entry: {entry}")
