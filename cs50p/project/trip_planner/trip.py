import re
import math
import requests
from currency_converter.main import CurrencyConverter
from trip_planner.destination import Destination

class Trip:
    CURRENCIES = ["USD", "CAD"]

    def __init__(self, traveler: str, currency: str, destination: Destination):
        self.traveler = traveler
        self.currency = currency
        self.destination = destination
        self._is_booked = False

    @property
    def traveler(self):
        return self._traveler

    @traveler.setter
    def traveler(self, traveler: str):
        if not (type(traveler).__name__ == 'str'):
            raise ValueError("Invalid Traveler's name")
        pattern = r"^[a-zA-Z\s]+$"
        match = re.search(pattern, traveler.strip())
        if not(match):
            raise ValueError("Invalid Traveler's name")
        self._traveler = traveler

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        if not (type(currency).__name__ == 'str'):
            raise ValueError("Invalid currency")
        currency = currency.upper()
        if (currency not in Trip.CURRENCIES):
            raise ValueError("Invalid currency")
        self._currency = currency

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, destination: Destination):
        if not destination:
            raise ValueError("Invalid destination")
        self._destination = destination

    @property
    def is_booked(self):
        return self._is_booked

    @is_booked.setter
    def is_booked(self, is_booked: bool):
        if not (type(is_booked).__name__ == 'bool'):
            raise ValueError("Invalid is_booked flag")
        self._is_booked = is_booked

    def book(self, amount: float) -> bool:
        try:
            float_amount = float(amount)
        except Exception:
            raise ValueError("Invalid Amount")

        if (self.is_booked == False and math.isclose(self.destination.cost, float_amount)):
            self.is_booked = True
            return True
        else:
            return False

    def cancel(self) -> str:
        if (self.is_booked == True):
            self.is_booked = False
            return f"The trip has been canceled. Refund: {self.destination.cost:.2f} {self.currency}"
        else:
            return "The trip is not booked"

    def get_cost_by_currency_rate(self) -> str:
        currency_converter = CurrencyConverter()

        token = "rc_live_35407404a45e4ca38a75b447a56c716e"
        response = requests.get(f"https://api.restcountries.com/countries/v5/names.common/{self.destination.country}?q=is&response_fields=currencies.code",
                                headers={"Authorization": f"Bearer {token}"})
        content = response.json()

        local_currency = content["data"]["objects"][0]["currencies"][0]["code"]
        local_cost = currency_converter.convert(self.destination.cost, self.currency, local_currency)

        return f"Cost: {self.destination.cost:.2f} {self.currency} = Equivalent Cost: {local_cost}"
