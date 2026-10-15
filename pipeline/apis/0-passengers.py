#!/usr/bin/env python3
"""
By using the Swapi API, create a method that returns
the list of ships that can hold a given number of passengers
"""
import requests


def availableShips(passengerCount):
    """
    returns the list of ships that can hold a given number of passengers
    If the list is empty, the method should return an empty list
    """
    url = "https://swapi-api.alx-tools.com/api/starships/"
    ships = []
    while url:
        response = requests.get(url)
        data = response.json()
        for ship in data['results']:
            if (
                ship["passengers"] != "n/a"
                and ship["passengers"] != "unknown"
                and ship["passengers"] != "0"
                and ship["passengers"] != "none"
            ):
                ship["passengers"] = ship["passengers"].replace(",", "")
                if int(ship["passengers"]) >= passengerCount:
                    ships.append(ship["name"])
        url = data["next"]
    return ships
