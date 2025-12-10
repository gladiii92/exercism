import math

def score(x, y):
    x = abs(x)
    y = abs(y)

    distance = math.sqrt((x - 0) ** 2 + (y - 0) ** 2)

    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    else:
      return 0

    return "fallback"



