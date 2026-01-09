def is_valid(isbn):
    
    
    
    # isbn = "3-598-21508-8"  # str, Input
    # isbn_clean = isbn.replace("-", "")  # str, jetzt nur noch 10 Zeichen
    # len(isbn_clean)  # int, Länge des Strings
    # isbn_clean[-1]  # str, letztes Zeichen
    
    # Input ist ein String von Zahlen 
    # Output ist ein Bool
    if isbn.count("-") == 3:
        
        if not ("-" == isbn[1] and "-" == isbn[5] and "-" == isbn[11]):
            return False
            
    elif isbn.count("-") != 0:
        return False
        
    isbn = isbn.replace("-", "")
    
    if len(isbn) != 10 or not isbn[:9].isdigit():
        return False

    total = 0    
    for idx in range(9):
        digit = int(isbn[idx])
        weight = 10 - idx
        total += digit * weight

    last_char = isbn[9]
    if last_char == "X":
        last_value = 10
    elif last_char.isdigit():
        last_value = int(last_char)
    else:
        return False
        
    total += last_value * 1

    return True if total % 11 == 0 else False
        
    # Edge-Cases:
    # leere eingabe = False
    # letzte Zahl (-1) darf NUR eine Zahl von 1-10 sein ODER ein X. Kein anderer Buchstabe
    # ISBN darf mit oder ohne Bindestriche sein, allerdings NUR an der richtigen Stelle!
    # NUR 10 Nummern sind erlaubt (außer die letzte, darf NUR ein X sein) + 3 Bindestriche

    
    # Falls benötigt.
    # isbn[1] == "-"
    # isbn[5] == "-"
    # isbn[11] == "-"

    # 1 Edge-Case muss noch raus -> Buchstabe zwischen den Zahlen!


    # Berechnung ist Nummer * 10 + Nummer * 9 (absteigend) % == 0
    # also ((isbn * i) + (isbn * i-1)) % == 0
