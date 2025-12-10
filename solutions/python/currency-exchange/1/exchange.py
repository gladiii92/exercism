"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    
    exchanged = budget / exchange_rate
    return exchanged


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    rest = budget - exchanging_value
    return rest


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    value_bills = number_of_bills * denomination
    return value_bills


def get_number_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    amount_bills = amount // denomination
    return amount_bills


def get_leftover_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    rest_amount = amount % denomination 
    return rest_amount


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange. 100.000
    :param exchange_rate: float - the unit value of the foreign currency. 10.61
    :param spread: int - percentage that is taken as an exchange fee. 10
    :param denomination: int - the value of a single bill. 1
    :return: int - maximum value you can get.
    """
    
    spread_deci = spread / 100 # 0.1
    rate_with_spread = exchange_rate * (1 + spread_deci) # 10.61 * (1+0.1 = 1.1)
    new_currency = budget / rate_with_spread # 100000 / 11,671 = 8568,24608
    exchangeable = (new_currency // denomination) * denomination # (8568,24608 // 1) * 1 = 8568
    return exchangeable