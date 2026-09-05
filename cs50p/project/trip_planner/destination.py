import re
import csv

class Destination:
    COUNTRIES = ["Canada", "USA", "Spain", "Italy", "France", "Australia"]

    destinations = []

    def __init__(self, country: str, cost: float, emoji: str):
        self.country = country
        self.cost = cost
        self.emoji = emoji

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country: str):
        if not (type(country).__name__ == 'str'):
            raise ValueError("Invalid country")
        if (country not in Destination.COUNTRIES):
            raise ValueError("Invalid country")
        self._country = country

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost: float):
        try:
            float_cost = float(cost)
        except Exception:
            raise ValueError("Invalid Cost")
        if (float_cost < 0):
            raise ValueError("Invalid Cost")
        self._cost = float_cost

    @property
    def emoji(self):
        return self._emoji

    @emoji.setter
    def emoji(self, emoji: str):
        if not (type(emoji).__name__ == 'str'):
            raise ValueError("Invalid emoji")
        pattern = r"^:globe_showing_(Americas|Europe-Africa|Asia-Australia):$"
        match = re.search(pattern, emoji.strip())
        if not(match):
            raise ValueError("Invalid emoji")
        self._emoji = emoji

    @classmethod
    def get_destinations(cls) -> list:
        if (len(cls.destinations) == 0):
            with open("trip_planner/destinations.csv", "r") as destinations_file:
                reader = csv.DictReader(destinations_file)
                for d in reader:
                    cls.destinations.append(Destination(d["Country"], float(d["Cost"]), d["Emoji"]))
        return cls.destinations
