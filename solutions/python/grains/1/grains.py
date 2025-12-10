def square(number): # XX squares hat das Chessboard
    if number > 0 and number < 65:
        pass
    else:
        raise ValueError("square must be between 1 and 64")
 
    # square/number 1 = 1 grain
    # square/number 2 = 2 grain
    # square/number 3 = 4 grain
    # square/number 4 = 8 grain etc.
    a = 1
    b = 1

    for i in range(1, number): # 4 = number / square
        a = a * 2
        b = b + a
    return a
    
def total():
    a = 1
    b = 1
    for i in range(1, 64):
        a *= 2
        b += a
    return b