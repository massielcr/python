# TRIP PLANNER
#### Video Demo:  <[CS50P Trip Planner](https://www.youtube.com/watch?v=dEkcxxptcZk)>
#### Description:

Trip Planner is a Python application that allows users to create a trip and execute basic actions on it. The user flow of the application is as follows:
- The app prompts the user to enter their name.
- The app prompts the user to enter their preferred currency (USD or CAD).
- The app displays a list of predefined destinations and prompts the user to make a selection based on the offered destinations.
- Once the selection is made, a trip is created and the app prompts the user for the amount due (the cost of the selected destination). If the amount entered by the user matches the cost of the trip, a booking is completed successfully.
- After successfully booking the trip, the user can choose to view the equivalent trip cost in the destination country’s currency based on current exchange rates, cancel the trip, or exit the program.

#### Project Structure:

```text
.
|-- trip_planner/
|   |-- destinations.csv
|   |-- destination.py
|   |-- trip.py
|-- project.py
|-- test_project.py
|-- requirements.txt
|-- README.md
```

#### Project Files and Implementation:

*project.py:*

*project.py* is the primary application file. It contains the main() function, which serves as the entry point for the program, prompting the user for all required information and handling the execution flow outlined in the [Description](#description) section. As mentioned, its implementation covers the collection of traveler information, the selection of a destination, the creation of a trip, the execution of a booking request, and the management of additional user actions, such as requesting currency conversions and trip cancellations. In addition to main(), it includes the following helper functions:

- `create_trip(traveler, currency, destination)` creates a Trip object.
- `book_trip(trip, amount)` attempts to book the trip.
- `cancel_trip(trip)` cancels an existing booking.
- `get_cost_by_currency_rate(trip)` displays the trip cost converted to the local currency.

*test_project.py:*

Contains the test suite for functions in *project.py*. The tests cover validation for traveler names, currencies, countries, costs, and emojis required to successfully create a trip, and cover success and failure scenarios for bookings and trip cancellations.

*trip.py:*

Defines the Trip class, which represents a trip that a user can create. It handles the creation of Trip objects, including the following properties and their respective validations:

|Property      |  Type          |  Description                          |  Validation  |
|---           |---             |---                                    |---           |
|`traveler`    | `str`          | Traveler name                         | Composed of uppercase and lowercase letters, and spaces |
|`currency`    | `str`          | Traveler preferred currency           | One of the following values: `USD` or `CAD`             |
|`destination` | `Destination`  | Traveler destination                  | One of the options exposed by the Destination class method `get_destinations()` |
|`_is_booked`  | `bool`         | Indicates whether the trip is booked  | True/False |

It also offers additional functionality as defined in the following methods:

- `book(amount)` checks the payment amount and marks the trip as booked if the amount matches the destination cost (trip price).
- `cancel()` cancels a booking and returns the refund message.
- `get_cost_by_currency_rate()` converts the destination cost to its local currency using an external API and a currency converter. The external API is available at `https://restcountries.com/apis/countries`, and the conversion is performed using the required `currency-converter-ext` library, as follows: `converter.convert(100, 'USD', 'EUR')`, as specified in the documentation.

*destination.py:*

Defines the Destination class, which represents a destination that a user can select to create a trip. It handles the creation of Destination objects, including the following properties and their respective validations:

|Property   |  Type  |  Description                 |  Validation  |
|---        |---     |---                           |---           |
| `country` | `str`  | Destination country name     | One of the following values: `Canada`, `USA`, `Spain`, `Italy`, `France`, or `Australia` |
| `cost`    | `float`| Destination cost (trip price)| Equal to or greater than 0 |
| `emoji`   | `str`  | Destination regional emoji   | One of the following values: `:globe_showing_Americas:`, `:globe_showing_Europe-Africa:`, or `:globe_showing_Asia-Australia:` |

It also includes the `get_destinations()` class method, which exposes a list of available destinations by reading predefined records from a CSV file.

*destination.csv:*

A CSV file that stores all destination data for the application. The CSV columns are as follows:

| Column     | Content                          |
|        --- | ---                              |
| `Country`  | Destination country name         |
| `Cost`     | Trip price                       |
| `Emoji`    | Emoji specific to the region     |

#### Project Dependencies

Application dependencies are listed in the `requirements.txt` file. Please install the packages accordingly. The file contents are listed below:

```
emoji
requests
currency-converter-ext
```

Of these dependencies, `currency-converter-ext` is worth highlighting. This Python library enables real-time currency conversion, making it possible to calculate equivalent costs in a destination country's local currency, which is one of the additional functions of the app.

#### Technical skills:

This application uses the following core concepts learned throughout the course:
- Exception handling
- Regular expressions
- File I/O
- API requests
- Object-oriented programming practices
- Use of published packages on the Python Package Index
- Unit testing
- Etc.
