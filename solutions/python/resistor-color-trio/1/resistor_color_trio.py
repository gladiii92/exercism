def label(colors):

    dict = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

    
    # Input ist eine liste mit str
    # Output soll ein Int sein + variabler str
    # Normalerweise keine Schleife nötig
    # Sonderfälle - Abfangbedingungen:
    # 4. Farbe ignorieren. (Ungültige Nummer unter 10?)

    first_color = dict[colors[0]] #str
    second_color = dict[colors[1]] #str

    third_color = dict[colors[2]] #str

    base_value = str(first_color) + str(second_color) #str + str
    end_value = base_value + "0" * third_color # str + 0 + str

    result = int(end_value)



    if result >= 1000000000:
        return f"{result // 1000000000} gigaohms"
    if result >= 1000000:
        return f"{result // 1000000} megaohms"
    elif result >= 1000:
        return f"{result // 1000} kiloohms"
    elif result <= 10:
        return f"{result} ohms"
    elif result == 0:
        result = 0
        return f"{result} ohms"
    else:
        return f"{end_value} ohms"