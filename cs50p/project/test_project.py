import pytest
import project
from trip_planner.trip import Trip
from trip_planner.destination import Destination

def test_create_trip_valid():
    trip = project.create_trip("John", "USD", Destination("Spain", 3250.50, ":globe_showing_Europe-Africa:"))
    assert trip.traveler == "John"
    assert trip.currency == "USD"
    assert trip.destination.country == "Spain"
    assert trip.destination.cost == 3250.50
    assert trip.destination.emoji == ":globe_showing_Europe-Africa:"
    assert trip.is_booked == False

def test_create_trip_invalid_traveler():
    with pytest.raises(ValueError):
        project.create_trip(1234, "USD", Destination("Spain", 3250.50, ":globe_showing_Europe-Africa:"))
    with pytest.raises(ValueError):
        project.create_trip("John1234", "USD", Destination("Spain", 3250.50, ":globe_showing_Europe-Africa:"))

def test_create_trip_invalid_currency():
    with pytest.raises(ValueError):
        project.create_trip("John", 123, Destination("Spain", 3250.50, ":globe_showing_Europe-Africa:"))
    with pytest.raises(ValueError):
        project.create_trip("John", "EUR", Destination("Spain", 3250.50, ":globe_showing_Europe-Africa:"))

def test_create_trip_invalid_destination():
    with pytest.raises(ValueError):
        project.create_trip("John", "USD", None)

def test_create_trip_invalid_country():
    with pytest.raises(ValueError):
        project.create_trip("John", "USD", Destination(123, 3250.50, ":globe_showing_Europe-Africa:"))
    with pytest.raises(ValueError):
        project.create_trip("John", "USD", Destination("Germany", 3250.50, ":globe_showing_Europe-Africa:"))

def test_create_trip_invalid_cost():
    with pytest.raises(ValueError):
        project.create_trip("John", "USD", Destination("Spain", "cat", ":globe_showing_Europe-Africa:"))
    with pytest.raises(ValueError):
        project.create_trip("John", "USD", Destination("Spain", -3250.50, ":globe_showing_Europe-Africa:"))

def test_create_trip_invalid_emoji():
    with pytest.raises(ValueError):
        project.create_trip("John", "USD", Destination("Spain", 3250.50, 123))
    with pytest.raises(ValueError):
        project.create_trip("John", "USD", Destination("Spain", 3250.50, ":globe_showing_Africa:"))

def test_book_trip_return_True():
    trip = Trip("John", "USD", Destination("Spain", 3250.50, ":globe_showing_Europe-Africa:"))
    assert project.book_trip(trip, 3250.50) == True

def test_book_trip_invalid_amount():
    trip = Trip("John", "USD", Destination("Spain", 3250.50, ":globe_showing_Europe-Africa:"))
    assert project.book_trip(trip, 2550.50) == False

def test_book_trip_invalid_amount_type():
    trip = Trip("John", "USD", Destination("Spain", 3250.50, ":globe_showing_Europe-Africa:"))
    with pytest.raises(ValueError):
        project.book_trip(trip, "cat")

def test_book_trip_already_booked():
    trip = Trip("John", "USD", Destination("Spain", 3250.50, ":globe_showing_Europe-Africa:"))
    trip._is_booked = True
    assert project.book_trip(trip, 3250.50) == False

def test_cancel_trip_booked():
    trip = Trip("John", "USD", Destination("Spain", 3250.50, ":globe_showing_Europe-Africa:"))
    trip._is_booked = True
    assert project.cancel_trip(trip) == "The trip has been canceled. Refund: 3250.50 USD"

def test_cancel_trip_not_booked():
    trip = Trip("John", "USD", Destination("Spain", 3250.50, ":globe_showing_Europe-Africa:"))
    assert project.cancel_trip(trip) == "The trip is not booked"

