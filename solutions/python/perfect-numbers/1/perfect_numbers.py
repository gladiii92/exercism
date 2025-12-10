def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # Edge-Cases
    if number == 1:
        return "deficient"
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    # Bestimmen ob eine Zahl perfekt, abundant oder deficient ist. (positive integers)
    number = abs(number) # macht eine Nummer positiv - ist zwar schon abgefangen, aber warum nicht ;-)

    # Berechnung?!
    liste = []
    for i in range(1, number):
        if number % i == 0:
            liste.append(i)
    summe = sum(liste)

    # Deficient
    if summe < number:
        return "deficient"
    # Abundant
    if summe > number:
        return "abundant"
    # Perfect
    if summe == number:
        return "perfect"            
    return "Fallback"
