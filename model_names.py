""" Function to validate IP addresses on data models """

import json


def import_model_names():
    """Function to import model names for validations"""

    with open("model_names.json", "r", encoding="utf-8") as names:
        model_names = json.load(names)
    return model_names
