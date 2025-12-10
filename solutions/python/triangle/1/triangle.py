def equilateral(sides): # alle Seiten gleich lang
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return a == b and b == c and a == c and all(sides)

def isosceles(sides): # mind. 2 Seiten gleich lang
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return a + b >= c and b + c >= a and a + c >= b and len(set(sides)) <= 2

def scalene(sides): # Alle Seiten unterschiedlich lang
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return a + b >= c and b + c >= a and a + c >= b and len(set(sides)) == 3