def commands(binary_str):
    leere_liste = []
    aktionen = ["wink", "double blink", "close your eyes", "jump"]
    aktionen_bits = binary_str[-4:]
    
    for index, num in enumerate(aktionen_bits[::-1]):
        if num == "1":
            leere_liste.append(aktionen[index])
    if binary_str[0] == "1":
        return leere_liste[::-1]
    else:
        return leere_liste