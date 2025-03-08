import json

import requests


def initialisation():
    """Initialisation of the data bus"""
    with open("config.json") as f:
        data_bus = json.load(f)
    return data_bus


# Random comment
def connect_to_api(data_bus):
    """connect to the API"""
    response = requests.get(data_bus["api"]).json()
    data_bus["api_response"] = response

    return data_bus


def process_response(data_bus):
    """Process the response from the API."""
    joke = data_bus["api_response"].get("setup", "No setup found")
    punchline = data_bus["api_response"].get("punchline", "No punchline found")
    print(f"Joke: {joke}")
    print(f"Punchline: {punchline}")

    return data_bus


if __name__ == "__main__":

    data_bus = initialisation()

    steps = [connect_to_api, process_response]

    for step in steps:
        data_bus = step(data_bus)
