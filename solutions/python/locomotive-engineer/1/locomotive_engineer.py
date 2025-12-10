"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*numbers):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(numbers)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    a, b, c, *rest = each_wagons_id
    new = [c, *missing_wagons, *rest, a, b]
    return new
    
def add_missing_stops(*args, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    #print(args) # ({'from': 'Berlin', 'to': 'Hamburg'},) ###Tuple
    #print(kwargs) # {'stop_1': 'Lepzig', 'stop_2': 'Hannover', 'stop_3': 'Frankfurt'}
    empty = []
    for key, val in kwargs.items():
        empty.append(val)
    stops = {"stops": empty} # {'stops': dict_values(['Lepzig', 'Hannover', 'Frankfurt'])}
    args = dict(*args)
    new = {**args, **stops} 
    #print(*new) # {'from': 'Berlin', 'to': 'Hamburg'}
    return new
    # Lösung muss so aussehen:
    # {'from': 'Berlin', 'to': 'Hamburg', 'stops': ['Lepzig', 'Hannover', 'Frankfurt']}

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    a, b, c = zip(*wagons_rows)
    return [[*a], [*b], [*c]]

    # Output should be:
    # [[(2, 'red'), (5, 'blue'), (3, 'orange')], [(4, 'red'), (9, 'blue'), (7, 'orange')], [(8, 'red'), (13,        'blue'), (11, 'orange')]]
