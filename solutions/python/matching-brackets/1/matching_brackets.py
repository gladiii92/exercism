def is_paired(input_string):
    # Mappe öffnende auf passende schließende Klammern
    pairs = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for char in input_string:
        if char in pairs:  # öffnende Klammer
            stack.append(char)

            
        elif char in pairs.values():  # char in .values -> ([{
            
            # Wenn nicht im Stack(Liste) -> FALSE // ODER // pairs[stack.pop()] ungleich aktuellem char -> False
            if not stack or pairs[stack.pop()] != char:
                return False  # kein passendes Gegenstück
                
    return not stack  # True, wenn Stack leer (alles gepaart)