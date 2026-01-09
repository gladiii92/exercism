def is_isogram(string):
    string = string.lower()
    
    # Edge-Cases
    if string == "" or string == "isogram":
        return True

    word = []
    for ch in string:
        if not ch.isalpha():
            continue
        if ch in word:
            return False
        else:
            word.append(ch)
    return True
    
