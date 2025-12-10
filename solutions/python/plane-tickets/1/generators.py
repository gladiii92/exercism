"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    letters = ["A", "B", "C", "D"]
    for letter in range(number):
        yield letters[letter % 4]

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """    
    letters = ["A", "B", "C", "D"]
    seat_number = 1
    seat_count = 0

    while seat_count < number:
        letter_index = (seat_number - 1) % 4
        row = (seat_number - 1) // 4 + 1

        if row == 13:
            seat_number += (4 - letter_index) 
            continue

        yield str(row) + letters[letter_index]
        seat_number += 1
        seat_count += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seat_gen = generate_seats(len(passengers))
    new_dict = {}
    for name in passengers:
        new_dict[name] = next(seat_gen)
    return new_dict

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for number in seat_numbers:  
        ticket_id = (number + flight_id).ljust(12, "0")
        yield ticket_id
