import sys
from emoji import emojize
from trip_planner.trip import Trip
from trip_planner.destination import Destination

def main():
    traveler = input("Name: ")
    currency = input("Currency: ")
    destinations = Destination.get_destinations()
    while (True):
        print("Please select a destination:")
        for i, d in enumerate(destinations):
            print(f"[{i + 1}]-", f"{d.country} ({d.cost} USD)")
        choice = input("choice: ")
        try:
            destination = destinations[int(choice)-1]
            break
        except Exception:
            pass

    trip = create_trip(traveler, currency, destination)

    while (True):
        amount = input(f"Please pay amount due {trip.destination.cost:.2f} {trip.currency} to book the trip: ")
        is_booked = book_trip(trip, amount)
        if (is_booked == True):
            print(f"Congratulations {trip.traveler}, you are going to {trip.destination.country}! {emojize(trip.destination.emoji, language='alias')}{emojize(":airplane:", language='alias')}!")
            break
        else:
            print("Failed booking")

    options = ["See local cost", "Cancel Trip", "Exit"]
    while (True):
        print("Please select an option:")
        for i, o in enumerate(options):
            print(f"[{i + 1}]-", f"{o}")
        option = input("option: ")
        match option:
            case "1":
                print(get_cost_by_currency_rate(trip))
            case "2":
                print(cancel_trip(trip))
                break
            case _ :
                break

    sys.exit(f"Bye {emojize(":dizzy:", language='alias')}")


def create_trip(traveler: str, currency: str, destination: Destination) -> Trip:
    return Trip(traveler, currency, destination)

def book_trip(trip: Trip, amount: float) -> bool:
    return trip.book(amount)

def cancel_trip(trip: Trip)-> str:
    return trip.cancel()

def get_cost_by_currency_rate(trip: Trip)-> str:
    return trip.get_cost_by_currency_rate()


if __name__ == "__main__":
    main()
