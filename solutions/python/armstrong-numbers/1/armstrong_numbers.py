def is_armstrong_number(number): 
    ergebnisse = []
    zahlen = [int(x) for x in str(number)]

    for zahl in zahlen:
        ergebnis = zahl ** len(zahlen) # das ist jetzt bei 153 = 1 125 27
        ergebnisse.append(ergebnis)

    summe = sum(ergebnisse)

    if summe == number:
        return True
    else:
        return False

    # Die Summen davon vergleiche ich dann mit der ursprungsnummer. Wenn gleich dann True, andernfalls False
