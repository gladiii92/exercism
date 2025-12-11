def resistor_label(colors):
    dict = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
    
    tolerance = {"grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5, "brown": 1, "red": 2, "gold": 5, "silver": 10}
    if dict[colors[0]] == 0:
        return f"0 ohms"
    tolerance_value = tolerance[colors[-1]]

    def format_value(val):
        return str(int(val)) if val == int(val) else str(val)
    
    if len(colors) == 4:  # 4-Band Widerstand
        first = dict[colors[0]]
        second = dict[colors[1]]
        multiplier = 10 ** dict[colors[2]]
        value = (first * 10 + second) * multiplier
    else:  # 5-Band Widerstand
        first = dict[colors[0]]
        second = dict[colors[1]]
        third = dict[colors[2]]
        multiplier = 10 ** dict[colors[3]]
        value = (first * 100 + second * 10 + third) * multiplier
        
    if value >= 1000000000:
        return f"{format_value(value / 1000000000)} gigaohms ±{tolerance_value}%"
    if value >= 1000000:
        return f"{format_value(value / 1000000)} megaohms ±{tolerance_value}%"
    elif value >= 1000:
        return f"{format_value(value / 1000)} kiloohms ±{tolerance_value}%"
    else:
        return f"{value} ohms ±{tolerance_value}%"