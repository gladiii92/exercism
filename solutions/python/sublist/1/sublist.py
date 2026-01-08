"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
UNEQUAL = 0
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3

def sublist(list_one, list_two):
    """
    Vergleicht zwei Listen und gibt zurück:
    - EQUAL, wenn die Listen identisch sind
    - SUBLIST, wenn list_one in list_two enthalten ist
    - SUPERLIST, wenn list_two in list_one enthalten ist
    - UNEQUAL, wenn keine der Bedingungen zutrifft
    """
    
    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_one, list_two):
        return SUBLIST
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL

def is_sublist(smaller, larger):
    """
    Prüft, ob `smaller` eine Teilmenge von `larger` ist.
    Leere Listen gelten als Sublist jeder Liste.
    """
    
    # Wenn kleine Liste leer -> True
    if not smaller:
        return True
        
    len_small, len_large = len(smaller), len(larger)
    # Wenn kleine Liste größer als die große Liste ist -> False
    if len_small > len_large:
        return False
    
    # Sliding-Window-Prinzip: prüfen ob Slice der längerne Liste == der kleinen Liste ist -> True
    for i in range(len_large - len_small + 1):
        if larger[i:i+len_small] == smaller: # z.B. larger[1 : 1 + 3] (Slice der großen Liste) gleich der kleinen Liste
            return True
    # Wenn durchgelaufen und kein Match -> False
    return False