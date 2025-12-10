def steps(number):
    # Fehlerabfangung
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
        
    # Setze count
    count = 0
    
    # Wir brauchen einen Zähler der jedes mal zählt wenn die number geteilt oder multipliziert wird.
    while number != 1: # solange number nicht 1 ist: n = 12
        if number % 2 == 0: # wenn gerade:
            number = number // 2
            count += 1
        elif number % 2 != 0: # wenn ungerade
            number = number * 3 + 1
            count += 1
            
    return count
