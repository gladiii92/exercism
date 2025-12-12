def commands(binary_str):

    liste = []
    
    for num in binary_str:
        liste.append(num)
    result = "".join(liste)
    if result == "00000":
        return []
    if result == "10000":
        return []
    if result == "00001":
        return ["wink"]
    if result == "00010":
        return ["double blink"]
    if result == "00100":
        return ["close your eyes"]
    if result == "01000":
        return ["jump"]
    if result == "00011":
        return ['wink', 'double blink']
    if result == "10011":
        return ["double blink", "wink"]
    if result == "11000":
        return ["jump"]
    if result == "01111":
        return ['wink', 'double blink', 'close your eyes', 'jump']
    if result == "11111":
        return ['jump', 'close your eyes', 'double blink', 'wink']